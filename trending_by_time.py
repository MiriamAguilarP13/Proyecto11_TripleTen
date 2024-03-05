import pandas as pd


trending = pd.read_csv("files/datasets/trending_by_time.csv")

trending.head()
trending.info()

trending['trending_date'] = pd.to_datetime(trending['trending_date'], format='mixed')

trending['trending_date'].dt.hour

trending.groupby(['category_title', 'trending_date'])['videos_count'].sum().sort_values(ascending= False).median()
