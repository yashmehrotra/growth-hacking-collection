import twitter
from time import sleep
from secret_settings import secrets

API = []
for s in secrets:
    API.append(twitter.Api(consumer_key=s['ckey'],
                           consumer_secret=s['csec'],
                           access_token_key=s['atkey'],
                           access_token_secret=s['atsec']))


names = [name.rstrip('\n') for name in open('screen_names.txt')]
api = API[0]
for name in names:
    try:
        f = api.CreateFriendship(screen_name=name)
        print f
        sleep(3)
    except Exception as e:
        print str(e)
