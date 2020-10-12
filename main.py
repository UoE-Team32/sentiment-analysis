import tweepy
import os
import re
from textblob import TextBlob
from dotenv import load_dotenv

# Load .env file and associated vars
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Begin streaming
class StreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            return False

    def on_status(self, status):
        # Only filter tweets containing English language
        if status.lang != "en":
            return

        # Analyse the tweet
        analysis = TextBlob(status.text)
        if analysis.sentiment.polarity > 0: 
            print('ID: ' + status.id_str + ', Polarity: Positive')
        elif analysis.sentiment.polarity == 0: 
            print('ID: ' + status.id_str + ', Polarity: Neutral')
        else: 
            print('ID: ' + status.id_str + ', Polarity: Negative')

streamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=streamListener)

myStream.filter(track=['#covid19'])