import twitter
from time import sleep
from settings import *
from secret_settings import secrets

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=AT_KEY,
                  access_token_secret=AT_SEC)


terms = [
 'Travel',
 'Football',
 'Art',
 'Food'
] 

def check_res(tweet, terms):
    global ht
    ht = ['#' + tag.text for tag in tweet.hashtags]
    if any(i in ht for i in terms):
        return True
    return False

# API = []
# for s in secrets:
#     API.append(twitter.Api(consumer_key=s['ckey'],
#                            consumer_secret=s['csec'],
#                            access_token_key=s['atkey'],
#                            access_token_secret=s['atsec']))

with open('mined.csv', 'w') as f:
    f.write('screen_name,hashtag,tweet_id\n')
    try:
        #api = API[0]
        for t in terms:
            x = api.GetSearch(term=t,count=100,include_entities=False)
            import ipdb;ipdb.set_trace()
            for tweet in x:
                # f.write('{0},#{1},{2}\n'.format(tweet.user.screen_name, t, str(tweet.id)))
                # print tweet.user.screen_name
                pass
            print 'Done ' + t
            sleep(5)
    except twitter.TwitterError as e:
        print str(e)
    except Exception as e:
        print str(e)

print '\n\n\nFinished\n\n\n'
