# %%
import numpy as np
import pandas as pd

from df_viewer import view_df

# %%
"""
Q: Create a panda dataframe using an array of arrays
"""
df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
    columns=["A", "B", "C"],
    index=["x", "y", "z", "zz"],
)

# %%
"""
Q: What are the methods with which one can get the ideas of a dataframe
"""
# print(df.head())
# print(df.tail(2))
# print(df.columns)
# print(df.index.tolist())
# print(df.info())
# print(df.describe())
# print(df.nunique())
# print(df.shape)
# print(df.size)

# %%
"""
Q: Find out all the unique values in a column of a panda dataframe
"""
print(df["A"].unique())

# %%
"""
Q: How to load data in pandas dataframe from csv, excel and parquet files
"""
# csv file
coffee = pd.read_csv("./warmup-data/coffee.csv")
bios = pd.read_csv("./data/bios.csv")
# parquet file
results = pd.read_parquet("./data/results.parquet")
# excel file
olympics_data = pd.read_excel("./data/olympics-data.xlsx", sheet_name="results")

# %%
"""
Q: How can you get 5 random rows from a pandas dataframe
"""
print(coffee.sample(5))  # Pass in random_state to make deterministic

# %%
# loc allows to filter by rows and columns
# coffee.loc[Rows, Columns]
print(coffee.loc[0])

# %%
print(coffee.loc[[0, 1, 5]])

# %%
print(coffee.loc[5:9, ["Day", "Units Sold"]])

# %%
# With .iloc the upper index is not inclusive where with .loc it was inclusive
print(coffee.iloc[:, [0, 2]])

# %%
coffee.index = coffee["Day"]
coffee.head()

# %%
print(coffee.loc["Monday":"Wednesday", ["Day", "Units Sold"]])

# %%
print(coffee.iloc[0:7, [0, 2]])

# %%
coffee = pd.read_csv("./warmup-data/coffee.csv")

# %%
coffee.loc[1:3, "Units Sold"] = 10

# %%
# Optimized way to get single values (.at & .iat)
print(coffee.at[0, "Units Sold"])

# %%
print(coffee.iat[3, 1])

# %%
# Getting Columns
print(coffee.Day)

# %%
print(coffee["Day"])

# %%
# Sort values
print(coffee.sort_values(["Units Sold"], ascending=False))

# %%
print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[0, 0]))

# %%
# Iterate over dataframe with for loop
for index, row in coffee.iterrows():
    print(index)
    print(row)
    print("Coffee Type of Row:", row["Coffee Type"])

# %%
# Filtering Data
print(bios.head())

# %%
print(bios.loc[bios["height_cm"] > 215])

# %%
print(bios.loc[bios["height_cm"] > 215, ["name", "height_cm"]])

# %%
# Short-hand syntax (without .loc)
print(bios[bios["height_cm"] > 215][["name", "height_cm"]])

# %%
# Multiple filter condition
print(bios[(bios["height_cm"] > 215) & (bios["born_country"] == "USA")])

# %%
# Filter by string conditions
print(bios[bios["name"].str.contains("keith", case=False)])

# %%
# Regex syntax
bios[bios["name"].str.contains("keith|patrick", case=False)]
# Other cool regex filters

# Find athletes born in cities that start with a vowel:
vowel_cities = bios[bios["born_city"].str.contains(r"^[AEIOUaeiou]", na=False)]

# Find athletes with names that contain exactly two vowels:
two_vowels = bios[
    bios["name"].str.contains(
        r"^[^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*$",
        na=False,
    )
]

# Find athletes with names that have repeated consecutive letters (e.g., "Aaron", "Emmett"):
repeated_letters = bios[bios["name"].str.contains(r"(.)\1", na=False)]

# Find athletes with names ending in 'son' or 'sen':
son_sen_names = bios[bios["name"].str.contains(r"son$|sen$", case=False, na=False)]

# Find athletes born in a year starting with '19':
born_19xx = bios[bios["born_date"].str.contains(r"^19", na=False)]

# Find athletes with names that do not contain any vowels:
no_vowels = bios[bios["name"].str.contains(r"^[^AEIOUaeiou]*$", na=False)]

# Find athletes whose names contain a hyphen or an apostrophe:
hyphen_apostrophe = bios[bios["name"].str.contains(r"[-']", na=False)]

# Find athletes with names that start and end with the same letter:
start_end_same = bios[bios["name"].str.contains(r"^(.).*\1$", na=False, case=False)]

# Find athletes with a born_city that has exactly 7 characters:
city_seven_chars = bios[bios["born_city"].str.contains(r"^.{7}$", na=False)]

# Find athletes with names containing three or more vowels:
three_or_more_vowels = bios[
    bios["name"].str.contains(r"([AEIOUaeiou].*){3,}", na=False)
]

# %%
# Don't use regex search (exact match)
print(bios[bios["name"].str.contains("keith|patrick", case=False, regex=False)])

# %%## isin method & startswith
print(
    bios[
        bios["born_country"].isin(["USA", "FRA", "GBR"])
        & (bios["name"].str.startswith("Keith"))
    ]
)

# %%
# Query Function
print(bios.query('born_country == "USA" and born_city == "Seattle"'))

# %%
# Adding or Removing Columns
print(coffee.head())

# %%
coffee["price"] = 4.99

# %%
coffee["new_price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)

# %%
print(coffee)

# %%
coffee.drop(columns=["price"], inplace=True)

# the below would also have worked
# coffee = coffee.drop(columns=['price'])

# %%
coffee = coffee[["Day", "Coffee Type", "Units Sold", "new_price"]]

# %%
coffee["revenue"] = coffee["Units Sold"] * coffee["new_price"]

# %%
print(coffee)

# %%
coffee.rename(columns={"new_price": "price"}, inplace=True)

# %%
bios_new = bios.copy()

# %%
bios_new["first_name"] = bios_new["name"].str.split(" ").str[0]

# %%

# %%
print(bios_new.query('first_name == "Keith"'))

# %%
bios_new["born_datetime"] = pd.to_datetime(bios_new["born_date"])

# %%
bios_new["born_year"] = bios_new["born_datetime"].dt.year

# %%
print(bios_new[["name", "born_year"]])

# %%
bios_new.to_csv("./data/bios_new.csv", index=False)

# %%
bios["height_category"] = bios["height_cm"].apply(
    lambda x: "Short" if x < 165 else ("Average" if x < 185 else "Tall")
)


# %%
def categorize_athlete(row):
    if row["height_cm"] < 175 and row["weight_kg"] < 70:
        return "Lightweight"
    elif row["height_cm"] < 185 or row["weight_kg"] <= 80:
        return "Middleweight"

    else:
        return "Heavyweight"


bios["Category"] = bios.apply(categorize_athlete, axis=1)

# %%
print(bios.head())

# %%
# Merging & Concatenating Data
nocs = pd.read_csv("./data/noc_regions.csv")

# %%
bios_new = pd.merge(bios, nocs, left_on="born_country", right_on="NOC", how="left")

# %%
bios_new.rename(columns={"region": "born_country_full"}, inplace=True)

# %%
usa = bios[bios["born_country"] == "USA"].copy()
gbr = bios[bios["born_country"] == "GBR"].copy()

# %%
new_df = pd.concat([usa, gbr])

# %%
print(new_df.tail())

# %%
combined_df = pd.merge(results, bios, on="athlete_id", how="left")

# %%
print(combined_df.head())

# %%
# Handling Null Values
coffee.loc[[2, 3], "Units Sold"] = np.nan

# %%
# Make sure to set this to your Units Sold column if you want these changes to stick
print(coffee["Units Sold"].fillna(coffee["Units Sold"].mean()))

# %%
# coffee['Units Sold'] = coffee['Units Sold'].interpolate()
print(coffee["Units Sold"].interpolate())

# %%
coffee.dropna(
    subset=["Units Sold"]
)  # Use inplace=True if you want to update the coffee df

# %%
coffee[coffee["Units Sold"].notna()]

# %%
print(coffee)

# %%
# Aggregating Data
print(bios.head())

# %%
print(bios["born_city"].value_counts())

# %%
print(bios[bios["born_country"] == "USA"]["born_region"].value_counts().head(10))

# %%
print(bios[bios["born_country"] == "USA"]["born_region"].value_counts().tail(25))

# %%
# Groupby function in Pandas
print(coffee.groupby(["Coffee Type"])["Units Sold"].sum())

# %%
print(coffee.groupby(["Coffee Type"])["Units Sold"].mean())

# %%
print(
    coffee.groupby(["Coffee Type", "Day"]).agg({"Units Sold": "sum", "price": "mean"})
)

# %%
# Pivot Tables
pivot = coffee.pivot(columns="Coffee Type", index="Day", values="revenue")
print(pivot.sum())

# %%
print(pivot.sum(axis=1))

# %%
# Using datetime with Groupby
bios["born_date"] = pd.to_datetime(bios["born_date"])
bios["month_born"] = bios["born_date"].dt.month
bios["year_born"] = bios["born_date"].dt.year
bios.groupby([bios["year_born"], bios["month_born"]])[
    "name"
].count().reset_index().sort_values("name", ascending=False)

# %%
# Advanced Functionality
latte = coffee[coffee["Coffee Type"] == "Latte"].copy()
latte["3day"] = latte["Units Sold"].rolling(3).sum()

# %%
print(latte)

# %%
# !pip install pyjanitor
# import janitor

# %%
# print(coffee.clean_names())

# %%
# !pip install skimpy
# from skimpy import skim
# skim(results)

# %%
# coffee.info()

# %%
# New Functionality
results_numpy = pd.read_csv("./data/results.csv")
results_arrow = pd.read_csv(
    "./data/results.csv", engine="pyarrow", dtype_backend="pyarrow"
)

# %%
print(results_numpy.info())

# %%
print(results_arrow.info())

# %%
filtered_bios = bios[
    (bios["born_region"] == "New Hampshire") | (bios["born_city"] == "San Francisco")
]
print(bios.head())

# %%
import pandas as pd

# Creating a DataFrame
data = {
    "Date": [
        "2024-05-01",
        "2024-05-01",
        "2024-05-01",
        "2024-05-02",
        "2024-05-02",
        "2024-05-03",
        "2024-05-03",
        "2024-05-03",
    ],
    "Item": [
        "Apple",
        "Banana",
        "Orange",
        "Apple",
        "Banana",
        "Orange",
        "Apple",
        "Orange",
    ],
    "Units Sold": [30, 21, 15, 40, 34, 20, 45, 25],
    "Price Per Unit": [1.0, 0.5, 0.75, 1.0, 0.5, 0.75, 1.0, 0.75],
    "Salesperson": ["John", "John", "John", "Alice", "Alice", "John", "Alice", "John"],
}
df = pd.DataFrame(data)

# %%
pivot_table = pd.pivot_table(
    df, values="Units Sold", index="Date", columns="Item", aggfunc="sum"
)
print(pivot_table)


import matplotlib.pyplot as plt

# %%
import pandas as pd

# Assuming your DataFrame is named 'bios' and already loaded
# First, filter out rows where the height_cm data is missing
bios_filtered = bios.dropna(subset=["height_cm"])

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(bios_filtered["height_cm"], bins=20, color="blue", edgecolor="black")

plt.title("Distribution of Athlete Heights in Olympics")
plt.xlabel("Height in cm")
plt.ylabel("Number of Athletes")
plt.grid(True)

# Using a logarithmic scale for the y-axis if the data spread is wide
plt.yscale("log")

plt.show()
