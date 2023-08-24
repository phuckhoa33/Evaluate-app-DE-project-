import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('/home/phuckhoa/Documents/evaluate_application/Scraping/config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_query = 'Python programming'


# Perform the search
search_results = api.search(q=search_query, count=10)

# Print search results
for tweet in search_results:
    print(f"{tweet.user.screen_name}: {tweet.text}\n")
