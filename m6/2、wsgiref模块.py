from wsgiref.simple_server import make_server

def application(environ,start_response):

    start_response('200 OK',[('Content-Type','text/html')])
    path = environ.get('PATH_INFO')

    if path == '/login':
        with open('./html/login.html','rb') as f:
            fdata = f.read()
    else:
        with open('./html/index.html','rb') as f:
            fdata = f.read()
    return [fdata]

httped = make_server('',8802,application)

httped.serve_forever()