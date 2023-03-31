from time import sleep
from web_scraping import getPsnData, getSteamData
from api import createApi

api = createApi()

def createPsnTweet():
    title, list_games, more_games = getPsnData()

    if len(title) <= 280 and len(list_games) <= 280 and len(more_games) <= 280:
        try:
            tweet = api.update_status_with_media(status=title, filename='images\psn_ofertas.png')

            sleep(5)

            tweet_reply = api.update_status(in_reply_to_status_id=tweet.id, status=list_games)

            sleep(5)

            api.update_status(in_reply_to_status_id=tweet_reply.id, status=more_games)

            print("\n\n--tweets sobre as oferdas da psn enviados com sucesso--\n\n")
        except Exception as error:
            print(error)
    else:
        print(f"\n\ntweet longo, possuí {len(title)} caracteres e suas respostas {len(list_games)} e {len(more_games)}\n\n")

def createSteamTweet():
    title, list_games, more_games = getSteamData()

    if len(title) <= 280 and len(list_games) <= 280 and len(more_games) <= 280:
        try:
            tweet = api.update_status_with_media(status=title, filename='images\steam_ofertas.jpg')

            sleep(5)

            tweet_reply = api.update_status(in_reply_to_status_id=tweet.id, status=list_games)

            sleep(5)
            
            api.update_status(in_reply_to_status_id=tweet_reply.id, status=more_games)

            print("\n\n--tweets sobre as oferdas da steam enviados com sucesso--\n\n")
        except Exception as error:
            print(error)
    else:
        print(f"\n\nTweet longo, possuí {len(list_games)} caracteres e {len(more_games)}\n\n")
