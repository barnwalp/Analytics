import os
import pandas as pd


path = os.path.join(os.getcwd(), 'datasets', 'pandas_official_database', 'data')
file = os.path.join(path, 'cast.csv')

# Will display all columns of the dataframe
pd.set_option('max_columns', None)
df = pd.read_csv(file)

# Filtering
filterd_df = df[(df['year'] > 2010) & (df['name'].str.startswith('B'))]

# Sorting
filterd_df.sort_values('title')
filterd_df.sort_index()

# Null values
df_null = df[df['n'].isnull()]

# Groupby with column-names
df_year = df.groupby('year').size()
df_year = df.groupby(['year', 'title']).size()

# Groupby with custom field
# custom groupby based on decade
decade = df['year']//10 * 10
df_dec = df.groupby(decade).size()
df_dec_actor = df.groupby([(df['year']//10*10), 'type']).size()

# indexing - cause performance imrovement, speed will further icnrease
# if the index are in sorted order
df = df.set_index(['title']).sort_index()


