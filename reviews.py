# add your code here

import pandas as pd
import zipfile 

zip_file_path = 'data/winemag-data-130k-v2.csv.zip'
csv_file_name = 'winemag-data-130k-v2.csv'

with zipfile.ZipFile(zip_file_path, 'r') as zippity:
    with zippity.open(csv_file_name) as f:
        df = pd.read_csv(f)

summary = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()

summary['points'] = summary['points'].round(1)

summary.to_csv('data/reviews-per-country.csv', index=False)

print("`reviews.py` has written data to the file `data/reviews-per-country.csv`")