import feedparser
from bottle import default_app, route, static_file


@route('/')
def hello_world():

    main_url = "https://devquestions.wordpress.com/feed"

    all_questions = []
    
    try_load_next = True
    page = 1
    
    while try_load_next:

        if page == 1:
            url = main_url
        else:
            url = main_url + "/?paged=" + str(page)
        
        feed = feedparser.parse(url)

        for post in feed.entries:
            
            question = post.title
            
            all_questions.append(question)
            
        page = page + 1
        
        try_load_next = len(feed.entries) > 0

    return str(len(all_questions))

@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root="static/")

application = default_app()

