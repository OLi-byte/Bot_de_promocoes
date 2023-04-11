from api import createApi
from bs4 import BeautifulSoup
import requests
import re
import os


class TwitterBot:
    def __init__(self) -> None:
        '''instância as variáveis iniciais do bot.'''
        self.api = createApi()
        self.psn_url = 'https://store.playstation.com/pt-br/category/35027334-375e-423b-b500-0d4d85eff784/1'
        self.steam_url = 'https://store.steampowered.com/search/?specials=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
        self.psn_deals_url = 'https://store.playstation.com/pt-br/pages/deals'
        self.steam_deals_url = 'https://store.steampowered.com/search/?specials=1'

    def getPsnListGames(self):
        '''Limpa o console e exibe o texto que será enviado no próximo tweet sobre a loja Psn Store.'''
        self.clear()
        for i in self.getPsnData():
            print(i + "\n")

    def getSteamListGames(self):
        '''Limpa o console e exibe o texto que será enviado no próximo tweet sobre a loja Steam.'''
        self.clear()
        for i in self.getSteamData():
            print(i + "\n")

    def getPsnData(self) -> tuple:
        '''Retorna uma tupla com o título e a lista de jogos em promoção retirada da primeira página
        da loja Psn Store através de web scraping.
        -> tuple'''
        site = requests.get(self.psn_url, headers=self.headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        titles = soup.find_all(
            'span', class_=re.compile("psw-t-body"), limit=19)
        prices = soup.find_all(
            'span', class_=re.compile("psw-m-r-3"), limit=19)

        list_games = []

        for i in titles:
            if titles.index(i) % 2 == 0:
                list_games.append(
                    "-> " + i.text + ":" f" {prices[titles.index(i)].text}")

        tweet_title = f"Novas ofertas na psn store: {self.psn_deals_url}\n\n#PSNDeals #PSNStore #PSNOffers"

        psn_deals = "\n\n".join(list_games[:5])

        more_deals = "\n\n".join(list_games[5:])

        return (tweet_title, psn_deals, more_deals)

    def getSteamData(self) -> tuple:
        '''Retorna uma tupla com o título e a lista de jogos em promoção retirada da primeira página
        da loja Steam através de web scraping.'''
        site = requests.get(self.steam_url, headers=self.headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        titles = soup.find_all('span', class_="title", limit=13)
        prices = soup.find_all('div', class_=re.compile(
            "search_price discounted"), limit=13)

        list_prices = []
        list_titles = []

        for i in prices:
            price = str(i.text).split(' ')
            list_prices.append(price[2])

        for i in titles:
            list_titles.append(
                "-> " + i.text + ":" f" R${list_prices[titles.index(i)]}")

        tweet_title = f"Novas ofertas na Steam: {self.steam_deals_url}\n\n#steamoffer #steamdeals #steamdiscounts"

        steam_deals = "\n\n".join(list_titles[:7])

        more_deals = "\n\n".join(list_titles[7:])

        return (tweet_title, steam_deals, more_deals)

    def postPsnTweet(self):
        '''Envia um tweet com um título e uma imagem presente no diretório local /images,
        sem seguida responde o próprio tweet enviando a lista de jogos em oferta na Psn Store.'''
        title, list_games, more_games = self.getPsnData()

        if len(title) <= 280 and len(list_games) <= 280 and len(more_games) <= 280:
            try:
                tweet = self.api.update_status_with_media(
                    status=title, filename='images\psn_ofertas.png')

                tweet_reply = self.api.update_status(
                    in_reply_to_status_id=tweet.id, status=list_games)

                self.api.update_status(
                    in_reply_to_status_id=tweet_reply.id, status=more_games)

                print("\n\n--tweets sobre as oferdas da psn enviados com sucesso--\n\n")
            except Exception as error:
                print(error)
        else:
            print(
                f"\n\ntweet longo, possuí {len(title)} caracteres e suas respostas {len(list_games)} e {len(more_games)}\n\n")

    def postSteamTweet(self):
        '''Envia um tweet com um título e uma imagem presente no diretório local /images,
        sem seguida responde o próprio tweet enviando a lista de jogos em oferta na Steam.'''
        title, list_games, more_games = self.getSteamData()

        if len(title) <= 280 and len(list_games) <= 280 and len(more_games) <= 280:
            try:
                tweet = self.api.update_status_with_media(
                    status=title, filename='images\steam_ofertas.jpg')

                tweet_reply = self.api.update_status(
                    in_reply_to_status_id=tweet.id, status=list_games)

                self.api.update_status(
                    in_reply_to_status_id=tweet_reply.id, status=more_games)

                print(
                    "\n\n--tweets sobre as oferdas da steam enviados com sucesso--\n\n")
            except Exception as error:
                print(error)
        else:
            print(
                f"\n\nTweet longo, possuí {len(list_games)} caracteres e {len(more_games)}\n\n")

    def menu(self):
        '''Exibe o menu de opções.'''
        print(
            "p - exibe lista de jogos da psn a ser enviada\n"
            "s - exibe lista de jogos da steam a ser enviada\n"
            "cp - faz um tweet das últimas promoções da psn store\n"
            "cs - faz um tweet das últimas promoções da steam\n"
            "q - sair\n"
        )

    def clear(self):
        '''Limpa o console.'''
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        bot = TwitterBot()
        bot.clear()
        bot.menu()
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
            case _:
                print("Digite uma opção válida!")
        input("Aperte qualquer tecla para voltar ao menu...")
