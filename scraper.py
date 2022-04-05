import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/45863470#tab-reviews"

response = requests.get(url)


page_dom = BeautifulSoup(response.text, "html.parser")

opinions = page_dom.select("div.js_product-review")
opinion = opinions.pop()

opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").text.strip()
rcmd = opinion.select_one("span.user-post__author-name").text.strip()
score = opinion.select_one("span.user-post__score-count").text.strip()
content = opinion.select_one("div.user-post__text").text.strip()
posted_on = opinion.select_one("span.user-post__published > time:nth-child(1)").text.strip()["datetime"]
bought_on = opinion.select_one("span.user-post__published > time:nth-child(2)").text.strip()["datetime"]

print(type(author))
print(opinion.prettify())

