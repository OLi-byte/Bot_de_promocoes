import tweepy
from configparser import ConfigParser

def createApi():
    #config
    config = ConfigParser()
    config.read("config.ini")

    api_key = config['Twitter']['api_key']
    api_key_secret = config['Twitter']['api_key_secret']
    access_token = config['Twitter']['access_token']
    access_token_secret = config['Twitter']['access_token_secret']

    #authentication
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api
