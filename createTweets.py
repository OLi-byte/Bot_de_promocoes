from time import sleep
from web_scraping import getPsnData, getSteamData
from api import createApi

api = createApi()

def createPsnTweet():
    psn_response = getPsnData()
    psn_title = psn_response[0]
    psn_list_games = (psn_response[1], psn_response[2])

    if len(psn_title) <= 280 and len(psn_list_games[0]) <= 280 and len(psn_list_games[1]) <= 280:
        try:
            tweet = api.update_status_with_media(status=psn_title, filename='images\psn_ofertas.png')

            sleep(5)

            tweet_reply = api.update_status(in_reply_to_status_id=tweet.id, status=psn_list_games[0])

            sleep(5)

            api.update_status(in_reply_to_status_id=tweet_reply.id, status=psn_list_games[1])

            print("tweets sobre as oferdas da psn enviados com sucesso")
        except Exception as error:
            print(error)
    else:
        print(f"tweet longo, possuí {len(psn_title)} caracteres e suas respostas {len(psn_list_games[0])} e {len(psn_list_games[1])}")

def createSteamTweet():
    steam_response = getSteamData()
    steam_title = steam_response[0]
    steam_list_games = (steam_response[1], steam_response[2])

    if len(steam_title) <= 280 and len(steam_list_games[0]) <= 280 and len(steam_list_games[1]) <= 280:
        try:
            tweet = api.update_status_with_media(status=steam_title, filename='images\steam_ofertas.jpg')

            sleep(5)

            tweet_reply = api.update_status(in_reply_to_status_id=tweet.id, status=steam_list_games[0])

            sleep(5)
            
            api.update_status(in_reply_to_status_id=tweet_reply.id, status=steam_list_games[1])

            print("tweets sobre as oferdas da steam enviados com sucesso")
        except Exception as error:
            print(error)
    else:
        print(f"Tweet longo, possuí {len(steam_list_games[0])} caracteres e {len(steam_list_games[1])}")