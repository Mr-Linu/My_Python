import pandas as pd

wine_reviews = pd.read_csv("dailyActivity_merged.csv")

print(wine_reviews.shape)
print(wine_reviews.head())


print(wine_reviews.country == "Italy")