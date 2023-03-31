from bs4 import BeautifulSoup
import requests
import re

def getPsnData():
    url = 'https://store.playstation.com/pt-br/category/35027334-375e-423b-b500-0d4d85eff784/1'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    titles = soup.find_all('span', class_=re.compile("psw-t-body"), limit=19)
    prices = soup.find_all('span', class_=re.compile("psw-m-r-3"), limit=19)

    list_titles = []
    list_prices = []

    for i in prices:
        list_prices.append(i.text)

    for i in titles:
        if titles.index(i) % 2 == 0 :
            list_titles.append("-> " + i.text + ":" f" {list_prices[titles.index(i)]}")

            
    tweet_title = ("Novas ofertas na psn store: https://store.playstation.com/pt-br/pages/deals")

    psn_deals = "\n\n".join(list_titles[:5])

    more_deals = "\n\n".join(list_titles[5:])

    return(tweet_title, psn_deals, more_deals)


def getSteamData():
    url = "https://store.steampowered.com/search/?specials=1"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    titles = soup.find_all('span', class_="title", limit=13)
    prices = soup.find_all('div', class_=re.compile("search_price discounted"), limit=13)

    list_prices = []
    list_titles = []

    for i in prices:
        price = str(i.text).split(' ')
        list_prices.append(price[2])

    for i in titles:
        list_titles.append("-> " + i.text + ":" f" R${list_prices[titles.index(i)]}")

    tweet_title = "Novas ofertas na Steam: https://store.steampowered.com/search/?specials=1"

    steam_deals = "\n\n".join(list_titles[:7])

    more_deals = "\n\n".join(list_titles[7:])

    return(tweet_title, steam_deals, more_deals)
