import requests
from bs4 import BeautifulSoup

url = "https://www.booking.com/hotel/pl/happy-tower.pl.html#tab-reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.txt, 'html.parser')

reviews = page_dom.select("li.review_new_item_blockp")


