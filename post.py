import twitter
from secret_settings import secrets
from time import sleep

API = []
mapping = {}


def init():
    for s in secrets:
        API.append(twitter.Api(consumer_key=s['ckey'],
                               consumer_secret=s['csec'],
                               access_token_key=s['atkey'],
                               access_token_secret=s['atsec']))

def post_tweet(api, message, reply_id):
    resp = api.PostUpdate(message, in_reply_to_status_id=int(reply_id))
    print api, message, reply_id

# Round Robin
def get_api():
    global API
    i = 0
    while True:
        yield API[i%len(API)]
        i += 1


# [screen_name, hashtag, tweet_id]
init()
user_data = [line.rstrip('\n') for line in open('1.csv')][1:]
count = 0
api = get_api()
for d in user_data:
    dd = d.split(',')
    ht = dd[1]
    tweet_id = int(dd[2])

    message = mapping[ht[1:]]
    post_tweet(api.next(), message, tweet_id)
    print ht
    count += 1
    print count
    sleep(5)

