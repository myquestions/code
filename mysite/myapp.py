
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, static_file

@route('/')
def hello_world():
    return serve_static("index.html")

@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root="mysite/static/")

application = default_app()

