import pandas as pd


df = pd.read_csv('donors.txt', index_col='id')
print(df)
