
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from My Questions! Now with changes from local env made on 2016-02-16!'

application = default_app()

