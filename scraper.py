import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/45863470#tab-reviews"

response = requests.get(url)


page_dom = BeautifulSoup(response.text, "html.parser")

opinions = page_dom.select("div.js_product-review")
opinion = opinions.pop(3)

opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").text.strip()
rcmd = opinion.select_one("span.user-post__author-name").text.strip()
score = opinion.select_one("span.user-post__score-count").text.strip()
content = opinion.select_one("div.user-post__text").text.strip()
posted_on = opinion.select_one("span.user-post__published > time:nth-child(1)").text.strip()["datetime"]
bought_on = opinion.select_one("span.user-post__published > time:nth-child(2)").text.strip()["datetime"]
useful_for = opinion.select_one("button.vote-yes > span").text.strip()
useful_for = opinion.select_one("button.vote-yes > span").text.strip()
pros = opinion.select_one("div.review-feature__item--positives ~ div.review-feature__item")
pros = [item.text.strip() for item in pros]
cons = opinion.select_one("div.review-feature__item--negatives ~ div.review-feature__item")
cons = [item.text.strip() for item in cons]


print(type(author))
print(opinion.prettify())

