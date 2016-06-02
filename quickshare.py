import SimpleHTTPServer
import SocketServer
import socket
import sys

PORT = 8000

Host = socket.gethostbyname(socket.gethostname())

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Your folder is Quickshared on :  ", Host+":8000"
httpd.serve_forever()
