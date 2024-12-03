import tweepy
from textblob import TextBlob
from dotenv import load_dotenv
import os

load_dotenv()
consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")

access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")

auth=tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
api=tweepy.API(auth)

# public_tweets=api.search_tweets('Trump') 
"""
    Will not work cause twitter api is not freeeeeeeeeeeeeeeeeee.
"""