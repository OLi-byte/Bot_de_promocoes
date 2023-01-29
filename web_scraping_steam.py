from bs4 import BeautifulSoup
import requests
import re

def getSteamData():
    url = "https://store.steampowered.com/search/?specials=1"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    titles = soup.find_all('span', class_="title", limit=20)
    prices = soup.find_all('div', class_=re.compile("search_price discounted"), limit=20)

    list_prices = []
    list_titles = []

    for i in prices:
        price = str(i.text).split(' ')
        list_prices.append(price[2])

    for i in titles:
        list_titles.append(i.text + ":" f" R${list_prices[titles.index(i)]}")

    tweet_title = "Novas ofertas na Steam: https://store.steampowered.com/search/?specials=1"

    steam_deals = (
        f"{list_titles[0]}\n\n"
        f"{list_titles[1]}\n\n"
        f"{list_titles[2]}\n\n"
        f"{list_titles[3]}\n\n"
        f"{list_titles[4]}\n\n"
        f"{list_titles[5]}\n\n"
        f"{list_titles[6]}"
    )

    more_deals = (
        f"{list_titles[7]}\n\n"
        f"{list_titles[8]}\n\n"
        f"{list_titles[9]}\n\n"
        f"{list_titles[10]}\n\n"
        f"{list_titles[11]}\n\n"
        f"{list_titles[12]}\n\n"
        f"{list_titles[13]}\n\n"
        f"{list_titles[14]}\n\n"
        f"{list_titles[15]}"
    )

    return(tweet_title, steam_deals, more_deals)