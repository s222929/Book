import os
import pandas as pd

print(*[filename.split('.')[0] for filename in os.listdir('./opinions')], sep='\n')

product_id = input('Please enter product id: ')

opinions = pd.read_json(f'opinions/{product_id}.json')

opinions_count = len(opinions)
pros_count = opinions['pros'].map(bool).sum()
cons_count = opinions['cons'].map(bool).sum()
average_score = opinions['score'].mean().round(2)

stars_reccomendation = pd.crosstab(opinions['score'], opinions['rcmd'], dropna=False)
print(stars_reccomendation)