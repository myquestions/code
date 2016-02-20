import json
from random import randint
from bottle import default_app, route, static_file


@route('/')
def show_random_question():

    all_questions = []

    with open('mysite/static/questions.json') as data_file:    
        all_questions = json.load(data_file)

    index = randint(0, len(all_questions) - 1)
    
    question = all_questions[index]

    return question["question"]

@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root="mysite/static/")

application = default_app()

