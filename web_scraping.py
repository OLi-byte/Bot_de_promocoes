from bs4 import BeautifulSoup
import requests
import re

def getData():
    url = 'https://store.playstation.com/pt-br/category/35027334-375e-423b-b500-0d4d85eff784/1'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    titles = soup.find_all('span', class_=re.compile("psw-t-body"))
    prices = soup.find_all('span', class_=re.compile("psw-m-r-3"))

    list_titles = []
    list_prices = []

    for i in prices:
        list_prices.append(i.text)

    j = 0
    for i in titles:
        list_titles.append(i.text + ":" f" {list_prices[j]}")
        j += 1

    psn_deals = ("Novas ofertas na psn store:\n\n"
    f"{list_titles[0]}\n"
    f"{list_titles[2]}\n"
    f"{list_titles[4]}\n"
    "https://store.playstation.com/pt-br/pages/deals")

    more_deals = (
        f"{list_titles[6]}\n"
        f"{list_titles[8]}\n"
        f"{list_titles[10]}\n"
        f"{list_titles[12]}"
        f"{list_titles[14]}\n"
    )

    even_more_deals = (
        f"{list_titles[16]}\n"
        f"{list_titles[18]}\n"
        f"{list_titles[20]}\n"
        f"{list_titles[21]}"
    )

    return(psn_deals, more_deals, even_more_deals)