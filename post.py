import twitter
from secret_settings import secrets
from time import sleep

API = []
mapping = {
 'AMA': "It's time for you to do some cool AMA. Try out znapin. Download now.",
 'Art': "Art isn't what you see but what you make others see - Showcase your creativity with znapin - link",
 'BigB': 'ang',
 'FOMO': "You dont wanna be the last one to join - FOMO 's Download it now",
 'Fashion': 'Flaunt your style - let others ape ! Beam your style',
 'Food': "Calories don't count on the weekend - vlog your foodventures on znapin - link",
 'Football': 'Family',
 'GivingMeLife': 'Znapin is giving me life ! YAS!',
 'Happy': 'znapin with those who make you happy - link',
 'HowTo': "We'll know something others don't . How do you do it? Tell it with znapin",
 'Life': 'life is short',
 'Lol': "If it's a crazy as shit - its got to be on znapin! link -",
 'Love': 'The good things in life are better with you. Create moments with your loved ones',
 'LoveWins': 'Some things are done best with those you love . Create fun stories with znapin - Download Now.',
 'RisingStar': 'Those who leave a trail of glitter are never forgotten - start yours with znapin - link',
 'Sickening': '',
 'Squad': 'Looking to do something fun with your squad - check out znapin - link',
 'Star': 'Those who leave a trail of glitter are never forgotten - start yours with znapin - link',
 'Startup': 'when you are ready to quit',
 'TBT': "The best TBT's are made on Znapin Stories. What would be yours? link",
 'TFW': 'Say what you feel',
 'Travel': 'A simple hello could lead to a Million things. Create amazing stories with strangers.. Get znapin! link -',
 'WorldRecord': 'Some thing fun can also create a record ! What would be your fun? Get started with Znapin - link',
 'YouNow': 'Show your crazy side up - become a big craze - check out znapin now - Download ->',
 'acting': 'got the skill? show off your talent on znapin ! take up a boom or more! link',
 'android': 'download now or be in FOMO android link',
 'androidgames': 'a real game with your friends - only much more real and fun - znapin - link',
 'app': 'You havent done it till you have tried znapin - link',
 'bae': "Znapin's Bae! You Bae? Download now - link",
 'celeb': 'Listen',
 'challenge': 'You gotta accept the challenge to win - link',
 'challenges': 'You gotta accept the challenge to win - link',
 'class': 'Get your class talking',
 'college': 'Get your college talking',
 'comedy': 'comedy is just a perspective - show your fun side with znapin - link',
 'competition': 'The most fun competitions ever - happening live on znapin - link',
 'crazy': 'if you are crazy you are popular - link',
 'delicious': 'got some delicious stuff happening - znapin it - link',
 'doe': 'his app znapin doe! link',
 'dramaqueen': 'Its not entertainment if it aint drama - show your best side - get znapin - link',
 'dub': 'set your dub video record with znapin - link',
 'dubwar': 'start the real dub wars on znapin - link',
 'fam': 'You havent got it till - you have done something fun with your #fam.',
 'fan': 'You aint a fan if you can mimic your fav celeb - try it out with znapin - link',
 'fleek': "Znapin's on fleek! Get it or get FOMO! Link",
 'followback': 'followback for some cool stuff - coming up every day on znapin - link',
 'fun': 'looking for something funtastic - get znapin',
 'funny': 'when you are funny everyone loves you - get znapin get loved. link',
 'funtastic': 'looking for something funtastic - get znapin',
 'gamenight': 'thinking of a game? Create yours with znapin - link',
 'games': 'thinking of a party game? Create yours with znapin - link',
 'girls': 'Girls who just dont take selfies but are fun - get znapin - link',
 'hella': 'The hella hot app you got to try - znapin - download now - link',
 'iPhone': 'Show your cool factor out with znapin - Download Now ->',
 'ios': 'download now or be in FOMO ios link',
 'iosgames': 'a real game with your friends - only much more real and fun - znapin - link',
 'justdoit': 'dont think twice - just do it - get znapin now - link',
 'kaboom': 'Time for some action - if you can do it better then them - you kaboom them - link',
 'leaderboard': 'Did i hear it right? Znapin has a leaderboard for Selfies?',
 'lit': "It's best to get znapin when you are #lit! Download now.",
 'meme': 'Now create video memes with znapin - link',
 'movie': 'Twist your favourite movie scenes with znapin - create your video memes. link',
 'newapp': 'download now or be in FOMO link',
 'nominate': 'Got some fun challenge? Nominate your friends with znapin - link',
 'party': 'thinking of a party game? Create yours with znapin - link',
 'partynight': 'thinking of a party game? Create yours with znapin - link',
 'pinch': 'Find someone cute - pinch em on znapin - link',
 'play': 'work',
 'rekt': 'get rekt',
 'rt': 'Challenge - Can you do a tongue twister which gets the most RT - Accepted ?!! head here : link',
 'school': 'Get your school talking',
 'selfie': 'Set your selfie record with znapin - link',
 'selfiewar': 'start the selfie wars for real on znapin - link',
 'tonguetwister': 'Its time for some fun - create fun videos with tongue twisters - link',
 'trunt': 'You wanna get trunt',
 'velfie': 'set your velfie record with znapin - link',
 'video': 'create the most fun videos with znapin - link',
 'win': 'You gotta accept the challenge to win - link',
 'yas': 'Yaaas ! Yas! Yasss! You got to get znapin. Download now - link'
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
user_data = [line.rstrip('\n') for line in open('mined.csv')][1:]

api = get_api()
for d in user_data:
    dd = d.split(',')
    ht = dd[1]
    tweet_id = int(dd[2])

    message = mapping[ht[1:]]
    post_tweet(api.next(), message, tweet_id)
    sleep(5)

