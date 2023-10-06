import pandas as pd

df_ratings = pd.read_csv(r'./ratings.csv')
df_ratings.drop(columns="timestamp", inplace=True)
df_ratings['rating'] *= 2
df_ratings['rating'].astype(int)
df_ratings.to_csv('./ratings_simplified.csv', index=False, header=True)