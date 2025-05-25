# %%
import pandas as pd

# %%
url = "https://en.wikipedia.org/wiki/List_of_Indian_metropolitan_areas_by_GDP"
tables = pd.read_html(url)
print(len(tables))

# %%
df = tables[0]
df.head()

# %%
df.info()

# %%
# df.drop(columns='Source', inplace=True)
df.head()
