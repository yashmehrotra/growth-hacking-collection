import twitter
from secret_settings import secrets
from time import sleep

API = []
mapping = {
 'AMA': "It's time for you to do some cool AMA. Try out znapin. Download now. - http://bit.ly/1Ql1QXC",
 'Art': "Art isn't what you see but what you make others see - Showcase your creativity with znapin - http://bit.ly/1Ql1QXC",
 'BigB': 'Create your own crazy theory - only on Znapin. Download Now http://bit.ly/1Ql1QXC',
 'FOMO': "You dont wanna be the last one to join - FOMO 's Download it now http://bit.ly/1Ql1QXC",
 'Fashion': 'Flaunt your style - let others ape ! Beam your style http://bit.ly/1Ql1QXC',
 'Food': "Calories don't count on the weekend - vlog your foodventures on znapin - http://bit.ly/1Ql1QXC",
 'Football': "Family, Friends, Food and Football, if that's you, znapin's for you - Download now. http://bit.ly/1Ql1QXC",
 'GivingMeLife': 'Znapin is giving me life ! YAS! http://bit.ly/1Ql1QXC',
 'Happy': 'znapin with those who make you happy - http://bit.ly/1Ql1QXC',
 'HowTo': "We'll know something others don't . How do you do it? Tell it with znapin http://bit.ly/1Ql1QXC",
 'Life': 'life is short, break the rules, gossip, get fun, get znapin http://bit.ly/1Ql1QXC', ########
 'Lol': "If it's a crazy as shit - its got to be on znapin! http://bit.ly/1Ql1QXC",
 'Love': 'The good things in life are better with you. Create moments with your loved ones http://bit.ly/1Ql1QXC',
 'LoveWins': 'Some things are done best with those you love . Create fun stories with znapin - Download Now. http://bit.ly/1Ql1QXC',
 'RisingStar': 'Those who leave a trail of glitter are never forgotten - start yours with znapin - http://bit.ly/1Ql1QXC',
 'Sickening': 'If you got it sickening - you have got to get it on znapin http://bit.ly/1Ql1QXC', #########
 'Squad': 'Looking to do something fun with your squad - check out znapin - http://bit.ly/1Ql1QXC',
 'Star': 'Those who leave a trail of glitter are never forgotten - start yours with znapin - http://bit.ly/1Ql1QXC',
 'Startup': 'when you are ready to quit you are closer then you think. The journey is worth preserving - do it with znapin! http://bit.ly/1Ql1QXC', #####
 'TBT': "The best TBT's are made on Znapin Stories. What would be yours? http://bit.ly/1Ql1QXC",
 'TFW': 'Say what you feel at znapin http://bit.ly/1Ql1QXC', #########
 'Travel': 'A simple hello could lead to a Million things. Create amazing stories with strangers.. Get znapin! http://bit.ly/1Ql1QXC -',
 'WorldRecord': 'Some thing fun can also create a record ! What would be your fun? Get started with Znapin - http://bit.ly/1Ql1QXC',
 'YouNow': 'Show your crazy side up - become a big craze - check out znapin now - Download -> http://bit.ly/1Ql1QXC',
 'acting': 'got the skill? show off your talent on znapin ! take up a boom or more! http://bit.ly/1Ql1QXC',
 'android': 'download now or be in FOMO android http://bit.ly/1Ql1QXC',
 'androidgames': 'a real game with your friends - only much more real and fun - znapin - http://bit.ly/1Ql1QXC',
 'app': 'You havent done it till you have tried znapin - http://bit.ly/1Ql1QXC',
 'bae': "Znapin's Bae! You Bae? Download now - http://bit.ly/1Ql1QXC",
 'celeb': 'Listen  smile, agree and then do whatever the F you were gonna do anyway. Agree? get znapin http://bit.ly/1Ql1QXC', #######
 'challenge': 'You gotta accept the challenge to win - http://bit.ly/1Ql1QXC',
 'challenges': 'You gotta accept the challenge to win - http://bit.ly/1Ql1QXC',
 'class': 'Get your class talking http://bit.ly/1Ql1QXC',
 'college': 'Get your college talking http://bit.ly/1Ql1QXC',
 'comedy': 'comedy is just a perspective - show your fun side with znapin - http://bit.ly/1Ql1QXC',
 'competition': 'The most fun competitions ever - happening live on znapin - http://bit.ly/1Ql1QXC',
 'crazy': 'if you are crazy you are popular - http://bit.ly/1Ql1QXC',
 'delicious': 'got some delicious stuff happening - znapin it - http://bit.ly/1Ql1QXC',
 'doe': 'his app znapin doe! http://bit.ly/1Ql1QXC',
 'dramaqueen': 'Its not entertainment if it aint drama - show your best side - get znapin - http://bit.ly/1Ql1QXC',
 'dub': 'set your dub video record with znapin - http://bit.ly/1Ql1QXC',
 'dubwar': 'start the real dub wars on znapin - http://bit.ly/1Ql1QXC',
 'fam': 'You havent got it till - you have done something fun with your #fam. http://bit.ly/1Ql1QXC',
 'fan': 'You aint a fan if you can mimic your fav celeb - try it out with znapin - http://bit.ly/1Ql1QXC',
 'fleek': "Znapin's on fleek! Get it or get FOMO! http://bit.ly/1Ql1QXC",
 'followback': 'followback for some cool stuff - coming up every day on znapin - http://bit.ly/1Ql1QXC',
 'fun': 'looking for something funtastic - get znapin http://bit.ly/1Ql1QXC',
 'funny': 'when you are funny everyone loves you - get znapin get loved. http://bit.ly/1Ql1QXC',
 'funtastic': 'looking for something funtastic - get znapin http://bit.ly/1Ql1QXC',
 'gamenight': 'thinking of a game? Create yours with znapin - http://bit.ly/1Ql1QXC',
 'games': 'thinking of a party game? Create yours with znapin - http://bit.ly/1Ql1QXC',
 'girls': 'Girls who just dont take selfies but are fun - get znapin - http://bit.ly/1Ql1QXC',
 'hella': 'The hella hot app you got to try - znapin - download now - http://bit.ly/1Ql1QXC',
 'iPhone': 'Show your cool factor out with znapin - Download Now -> http://bit.ly/1Ql1QXC',
 'ios': 'download now or be in FOMO ios http://bit.ly/1Ql1QXC',
 'iosgames': 'a real game with your friends - only much more real and fun - znapin - http://bit.ly/1Ql1QXC',
 'justdoit': 'dont think twice - just do it - get znapin now - http://bit.ly/1Ql1QXC',
 'kaboom': 'Time for some action - if you can do it better then them - you kaboom them - http://bit.ly/1Ql1QXC',
 'leaderboard': 'Did i hear it right? Znapin has a leaderboard for Selfies? http://bit.ly/1Ql1QXC',
 'lit': "It's best to get znapin when you are #lit! Download now. http://bit.ly/1Ql1QXC",
 'meme': 'Now create video memes with znapin - http://bit.ly/1Ql1QXC',
 'movie': 'Twist your favourite movie scenes with znapin - create your video memes. http://bit.ly/1Ql1QXC',
 'newapp': 'download now or be in FOMO http://bit.ly/1Ql1QXC',
 'nominate': 'Got some fun challenge? Nominate your friends with znapin - http://bit.ly/1Ql1QXC',
 'party': 'thinking of a party game? Create yours with znapin - http://bit.ly/1Ql1QXC',
 'partynight': 'thinking of a party game? Create yours with znapin - http://bit.ly/1Ql1QXC',
 'pinch': 'Find someone cute - pinch em on znapin - http://bit.ly/1Ql1QXC',
 'play': 'work and play at znapin http://bit.ly/1Ql1QXC', ######
 'rekt': 'get rekt at znapin http://bit.ly/1Ql1QXC', #######http://bit.ly/1Ql1QXC
 'rt': 'Challenge - Can you do a tongue twister which gets the most RT - Accepted ?!! head here : http://bit.ly/1Ql1QXC',
 'school': 'Get your school talking at znapinhttp://bit.ly/1Ql1QXC',
 'selfie': 'Set your selfie record with znapin - http://bit.ly/1Ql1QXC',
 'selfiewar': 'start the selfie wars for real on znapin - http://bit.ly/1Ql1QXC',
 'tonguetwister': 'Its time for some fun - create fun videos with tongue twisters - http://bit.ly/1Ql1QXC',
 'trunt': 'You wanna get trunt, get znapin http://bit.ly/1Ql1QXC',
 'velfie': 'set your velfie record with znapin - http://bit.ly/1Ql1QXC',
 'video': 'create the most fun videos with znapin - http://bit.ly/1Ql1QXC',
 'win': 'You gotta accept the challenge to win - http://bit.ly/1Ql1QXC',
 'yas': 'Yaaas ! Yas! Yasss! You got to get znapin. Download now - http://bit.ly/1Ql1QXC'
 }

def init():
    for s in secrets:
        API.append(twitter.Api(consumer_key=s['ckey'],
                               consumer_secret=s['csec'],
                               access_token_key=s['atkey'],
                               access_token_secret=s['atsec']))

def post_tweet(api, message, reply_id):
    resp = api.PostUpdate(message, in_reply_to_status_id=int(reply_id))
    print api, message, reply_id

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

