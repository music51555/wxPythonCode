import socketserver

class Set_Server(socketserver.BaseRequestHandler):

    def handle(self):
        print('new conn:',self.client_address)
        print(self.process_request())
        while True:
            data = self.request.recv(1024)
            self.request.send(data.upper())

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8081),Set_Server)
    server.serve_forever()