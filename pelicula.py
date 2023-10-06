import pandas as pd

df_movies = pd.read_csv(r'./movies.csv')
df_ratings = pd.read_csv(r'./ratings_simplified.csv')
df_ratings.sort_values('movieId', inplace=True)

# GET BEST MOVIES TO QUERY NEW USER

# get metrics
df_dev = df_ratings.groupby('movieId')['rating'].std()
df_mean = df_ratings.groupby('movieId')['rating'].mean()
df_count = df_ratings.groupby('movieId')['rating'].count()
# merge
df_metrics = pd.concat([df_count, df_mean, df_dev], axis=1)
df_metrics.columns = ['count', 'mean', 'deviation']
# filter
df_metrics.drop(df_metrics[df_metrics['count'] < 100].index, inplace = True)

# sort and add name to df_metrics
df_metrics.sort_values('count', ascending=False, inplace=True)
df_movies.set_index = 'movieId'
df_movies.drop(columns='genres', inplace=True)
df_metrics = pd.merge(df_metrics, df_movies, on='movieId', how='left')
print(df_metrics)




