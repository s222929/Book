from bs4 import BeautifulSoup
import requests
import json

def get_element(parent, selector, attribute = None, return_list = False):
    try:
        if return_list:
            return [item.text.strip() for item in parent.select(selector)]
        if attribute:
            return parent.select_one(selector)[attribute]
        return parent.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

opinion_elements = {
    "author":["span.user-post__author-name"],
    "rcmd": ["span.user-post__author-recomendation > em"],
    "score": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "posted_on": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "bought_on": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "useful_for": ["button.vote-yes > span"],
    "useless_for": ["button.vote-no > span"],
    "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True]
}

product_id = input("Please enter the product id: ")
url = f"https://www.ceneo.pl/{product_id}#tab=reviews"

all_opinions = []

while (url):
    print(url)
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, "html.parser")
    opinions = page_dom.select("div.js_product-review")

    for opinion in opinions:
        single_opinion = {
            key: get_element(opinion, *values)
            for key, values in opinion_elements.items() 
        }

        single_opinion["opinion_id"] = opinion["data-entry-id"]
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+get_element(page_dom,"a.pagination__next","href")
    except TypeError: 
        url = None

with open(f"opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)

