# %%
import numpy as np
import pandas as pd

# %%
url = "https://en.wikipedia.org/wiki/List_of_fatal_crowd_crushes"
tables = pd.read_html(url)
# count total items of tables
print(len(tables))

# %%
df = tables[4]
df.info()

# %%
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Deaths"] = pd.to_numeric(df["Est. Deaths"], errors="coerce")
df[df["Deaths"].isna()]

# %%
df.loc[8, "Deaths"] = 10
df.loc[27, "Deaths"] = 100
df.loc[31, "Deaths"] = 30

# %%
death_by_country = df.pivot_table(index="Country", values="Deaths", aggfunc="sum")
death_by_country.sort_values(by="Deaths", ascending=False)
