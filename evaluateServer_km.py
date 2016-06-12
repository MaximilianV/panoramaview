from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from evaluate import ModelServer
import cgi


class AnnotationService(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        #ctype, pdict = cgi.parse_header(self.headers['content-type'])
        #if ctype == 'application/x-turtle':
        #print self.rfile.read(int(self.headers['content-length']))
	text = ''
	if( 'reviewText=' in  self.path):
		text =self.path.split('reviewText=')[1]
		print 'Evaluating: ', text
	text = text.replace("%20", " ")
	self.model = ModelServer(text)
	
        self._set_headers()
	resp = "{{'value':"+ str(self.model.evaluate()) +"}{'request':" + str(text)  + "}}"
        self.wfile.write(str(resp))
        return


"""    def do_POST(self):
        #ctype, pdict = cgi.parse_header(self.headers['content-type'])
        #if ctype == 'application/x-turtle':
        #    postnif = self.rfile.read(int(self.headers['content-length']))
        self._set_headers()
        self.wfile.write(str("Hey there!!!"))
        return"""

def run(server_class=HTTPServer, handler_class=AnnotationService, port=12343):
    server_address = ('185.82.22.53', 9999)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
