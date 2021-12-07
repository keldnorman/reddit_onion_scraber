```
#!/usr/bin/env python3

import re
import praw
import pprint
from time import time, strftime, gmtime

client_id = 'xxxxxxxxxxxxxxxxxxxxxx'
user_agent = 'Finding onions (by u/keld_norman)'
client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

triggers = ['.onion']
#triggers = ['onion', 'tor', 'darkweb', 'darknet']

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

def extract_onion_links(html):
    long = re.compile(r'[A-Za-z2-7]{56}\.onion', re.DOTALL | re.MULTILINE)
    links = re.findall(long, html)
    return set(links)

start = time()
print('# Starting Reddit Stream Onion Analyzer')

for comment in reddit.subreddit('all').stream.comments():

  created = comment.created_utc
  if created > start:

        created = strftime("%d %b %Y %H:%M:%S", gmtime(created))

        sub = comment.subreddit
        # author = comment.author.name
        body = comment.body
        title = comment.link_title
        # link = comment.permalink

        if all(str(l) in title for l in triggers):
            print(f'# {created}: r/{sub}')
            links = extract_onion_links(title)
            for m in links:
                print('{0}'.format(m))

        if all(str(l) in body for l in triggers):
            print(f'# {created}: r/{sub}')
            links = extract_onion_links(body)
            for m in links:
                print('{0}'.format(m))
```
