# Book

## Single opinion structure on [Ceneo.pl](https://www.ceneo.pl/)
|Element|Selector|Variable|Data type|
|-------|--------|--------|---------|
|Opinion|div.js_product-review|opinion|bs4.element.Tag|
|Opinion id|\["data-entry-id"\]|opinion_id|str|
|Author|span.user-post__author-name|author|str|
|Recommendation|span.user-post__author-recomendation > em|rcmd|bool|
|Stars score|span.user-post__score-count|score|float|
|Content|div.user-post__text|content|str|
|List of advantagess|div.review-feature__item--positives ~ div.review-feature__item|pros|list[str]|
|List of disadvantagess|div.review-feature__item--negatives ~ div.review-feature__item|cons|list[str]|
|Date of posting opinion|span.user-post__published > time:nth-child(1)\["datetime"\]|posted_on|str|
|Date of purchasing product|span.user-post__published > time:nth-chil(2)\["datetime"\]|bought_on|str|
|For how many users useful|button.vote-yes > span|useful_for|int|
|For how many users useless|button.vote-no > span|useless_for|int|