from createTweets import createPsnTweet, createSteamTweet
from web_scraping import getPsnData, getSteamData


class TwitterBot:
    def __init__(self) -> None:
        pass
    
    def getPsnListGames(self):
        psnData = getPsnData()
        for i in psnData:
            print(i + "\n")

    def getSteamListGames(self):
        steamData = getSteamData()
        for i in steamData:
            print(i + "\n")

    def postPsnTweet(self):
        createPsnTweet()

    def postSteamTweet(self):
        createSteamTweet()

while True:
    bot = TwitterBot()

    print(
        "p - exibe lista de jogos da psn a ser enviada\n"
        "s - exibe lista de jogos da steam a ser enviada\n"
        "cp - faz um tweet das últimas promoções da psn store\n"
        "cs - faz um tweet das últimas promoções da steam\n"
        "q - sair\n"
    )

    option = input("Selecione um comdando acima: ")
    
    match option:
        case "p":
            bot.getPsnListGames()
        case "s":
            bot.getSteamListGames()
        case "cp":
            bot.postPsnTweet()
        case "cs": 
            bot.postSteamTweet()
        case "q":
            exit()

