import twitter
from time import sleep
from settings import *
from secret_settings import secrets

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=AT_KEY,
                  access_token_secret=AT_SEC)

terms = ['#selfie', '#instaselfie', '#insta']
ht = []

def check_res(tweet, terms):
    global ht
    ht = ['#' + tag.text for tag in tweet.hashtags]
    if any(i in ht for i in terms):
        return True
    return False

API = []
for s in secrets:
    API.append(twitter.Api(consumer_key=s['ckey'],
                           consumer_secret=s['csec'],
                           access_token_key=s['atkey'],
                           access_token_secret=s['atsec']))

with open('screen_names.txt', 'w') as f:
    try:
        #api = API[0]
        for t in terms:
            x = api.GetSearch(term=t,count=100,include_entities=False)
            for tweet in x:
                if check_res(tweet,terms):
                    f.write(tweet.user.screen_name + '\n')
                print tweet.user.screen_name
            sleep(2)
    except twitter.TwitterError as e:
        print str(e)
    except Exception as e:
        print str(e)

print '\n\n\nFinished\n\n\n'
