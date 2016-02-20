import json
from bottle import default_app, route, static_file


@route('/')
def show_random_question():

    all_questions = []

    with open('mysite/static/questions.json') as data_file:    
        all_questions = json.load(data_file)

    return str(len(all_questions))

@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root="mysite/static/")

application = default_app()

