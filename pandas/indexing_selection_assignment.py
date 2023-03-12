import pandas as pd

wine_data = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 8)


# selecting description column from the data
desc = wine_data['description']

# selecting the first value of the description column
first_description = desc[0]

# selecting first row all columns
first_row = wine_data.iloc[0, :]

# Selecting the first 10 values from the description column in reviews, assigning the result to variable
first_descriptions = wine_data.description.iloc[:10]

# Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
sample_reviews = wine_data.iloc[[1, 2, 3, 5, 8]]

# Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index
# labels 0, 1, 10, and 100

df = wine_data.iloc[[0, 1, 10, 100]]
df = df.get(['country', 'province', 'region_1', 'region_2'])

# Create a variable df containing the country and variety columns of the first 100 records.

df = wine_data.loc[0:99, ['country', 'variety']]

# Create a DataFrame italian_wines containing reviews of wines made in Italy
italian_wines = wine_data[wine_data.country == "Italy"]

# Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100)
# for wines from Australia or New Zealand.

top_oceania_wines = wine_data[wine_data.points.isin([95, 96, 97, 98, 99, 100]) &
                              wine_data.country.isin(['Australia', 'New Zealand'])]


