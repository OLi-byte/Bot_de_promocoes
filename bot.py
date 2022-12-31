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
list_games = response[0]
more_games = response[1]
even_more_deals = response[2]

if len(list_games) <= 280 and len(more_games) <= 280 and len(even_more_deals) <= 280:
    try:
        tweet = client.create_tweet(text=list_games)
        print(tweet.data['text'])

        sleep(10)

        client.create_tweet(in_reply_to_tweet_id=tweet.data['id'], text=more_games)

        sleep(10)

        client.create_tweet(in_reply_to_tweet_id=tweet.data['id'], text=even_more_deals)
    except Exception as error:
        print(error)
else:
    print(f"tweet longo, possuí {len(list_games)} caracteres e sua resposta {len(more_games)} e {len(even_more_deals)}")
    










