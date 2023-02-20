import tweepy
from configparser import ConfigParser
from time import sleep
from web_scraping_psn import getPsnData
from web_scraping_steam import getSteamData

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

def main():
    psn_response = getPsnData()
    psn_title = psn_response[0]
    psn_list_games = psn_response[1]
    psn_more_games = psn_response[2]

    steam_response = getSteamData()
    steam_title = steam_response[0]
    steam_list_games = steam_response[1]
    steam_more_games = steam_response[2]

    if len(psn_title) <= 280 and len(psn_list_games) <= 280 and len(psn_more_games) <= 280:
        try:
            tweet = api.update_status_with_media(status=psn_title, filename='images\psn_ofertas.png')
            print(tweet.text)

            sleep(5)

            tweet_reply = api.update_status(in_reply_to_status_id=tweet.id, status=psn_list_games)

            sleep(5)

            api.update_status(in_reply_to_status_id=tweet_reply.id, status=psn_more_games)
        except Exception as error:
            print(error)
    else:
        print(f"tweet longo, possuí {len(psn_title)} caracteres e suas respostas {len(psn_list_games)} e {len(psn_more_games)}")

    if len(steam_title) <= 280 and len(steam_list_games) <= 280 and len(steam_more_games) <= 280:
        try:
            tweet = api.update_status_with_media(status=steam_title, filename='images\steam_ofertas.jpg')
            print(tweet.text)

            sleep(5)

            tweet_reply = api.update_status(in_reply_to_status_id=tweet.id, status=steam_list_games)

            sleep(5)
            
            api.update_status(in_reply_to_status_id=tweet_reply.id, status=steam_more_games)
        except Exception as error:
            print(error)
    else:
        print(f"Tweet longo, possuí {len(steam_list_games)} caracteres e {len(steam_more_games)}")


if __name__ == "__main__":
    main()
    










