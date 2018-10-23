from wsgiref.simple_server import make_server

def application(environ,start_response):

    start_response('200 OK',[('Content-Type','text/temples')])
    path = environ.get('PATH_INFO')

    if path == '/login':
        with open('./temples/login.temples','rb') as f:
            fdata = f.read()
    else:
        with open('./temples/index.temples','rb') as f:
            fdata = f.read()
    return [fdata]

httped = make_server('',8802,application)

httped.serve_forever()