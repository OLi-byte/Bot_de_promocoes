import tweepy
from configparser import ConfigParser
from time import sleep
from web_scraping import getData

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

client = tweepy.Client(
    consumer_key= api_key,
    consumer_secret= api_key_secret,
    access_token= access_token,
    access_token_secret= access_token_secret,
)

response = getData()
title = response[0]
list_games = response[1]
more_games = response[2]

if len(title) <= 280 and len(list_games) <= 280 and len(more_games) <= 280:
    try:
        tweet = api.update_status_with_media(status=title, filename='loja.png')
        print(tweet.text)

        sleep(5)

        api.update_status(in_reply_to_status_id=tweet.id, status=list_games)

        sleep(5)

        api.update_status(in_reply_to_status_id=tweet.id, status=more_games)
    except Exception as error:
        print(error)
else:
    print(f"tweet longo, possuí {len(title)} caracteres e suas respostas {len(list_games)} e {len(more_games)}")
    










