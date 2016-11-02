# coding:utf-8

from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    for k, v in environ.items():
        print(k, v)
    return [b'<b>Hello world</b>']

httpd = make_server('127.0.0.1', 8000,  application)
httpd.serve_forever()