import feedparser
import json

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
        
        tags = [x.term for x in post.tags if x.term != u'DevQuestion']
        
        question = {
            "question": post.title,
            "tags": tags,
            "url": post.link
        }
        
        all_questions.append(question)
        
    page = page + 1
    
    try_load_next = len(feed.entries) > 0

with open('mysite/static/questions.json', 'w') as outfile:
    json.dump(all_questions, outfile)

