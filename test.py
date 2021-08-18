import requests
import pandas as pd
import datetime
from requests.api import get
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


def web_content_div(web_content,class_path):
    web_content_div = web_content.find_all("div",{"class" : class_path})

    try:
        spans = web_content_div[0].find_all("span")
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts


def real_time_price(stock_code):
    url = f"https://in.finance.yahoo.com/quote/TCS.NS?p=TCS.NS&.tsrc=fin-srch"
    #headers = {"USer-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    try: 
    
        r = requests.get(url)
        print(r.text)
        web_content = BeautifulSoup(r.text, "lxml")
        print(web_content)
        text = web_content_div(web_content,"My(6px) Pos(r) smartphone_Mt(6px)")
        print(text)
        if text != []:
            price,change = text[0], text[1]
        else:
            price,change = [], []
    except ConnectionError:
        price, change = [], []

    return price,change 


print(real_time_price("TCS.NS"))