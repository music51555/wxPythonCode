import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data=self.request.recv(1024)
            if data=='exit':
                break
            print('>>>%s'%data.decode('utf-8'))
            print(self.client_address)
            send_data=input('>>>:')
            self.request.send(send_data.encode('utf-8'))
        self.request.close()

if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)
    server.serve_forever()