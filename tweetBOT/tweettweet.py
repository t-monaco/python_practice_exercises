from dotenv import load_dotenv
import tweepy
import os
import time

load_dotenv()

CONSUMER_KEY = os.getenv('API_KEY')
CONSUMER_SECRET = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_SECRET_TOKEN')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = 'Python'
number_of_tweets = 5


for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print('I like that')
    except tweepy.TweepError as e:
        print(e)
    except StopIteration:
        break



# Generous BOT
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    # if follower == "Follower Name":
    #     follower.follw()
    #     break