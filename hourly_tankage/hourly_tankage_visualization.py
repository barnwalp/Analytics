# %%
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# %%
path = os.path.join(os.getenv("win_home"), "github_repo", "datasets", "iocl")
os.chdir(path)
df = pd.read_csv("hourly_tank_report.csv")
df.head()

# %%
plt.figure(figsize=(14, 8))
sns.lineplot(data=df, x="DATE AND TIME", y="OPENING STOCK(Ltr.)", hue="PRODUCT")

# %%
df_opening = df[df["OPENING STOCK(Ltr.)"] <= 3000]
df_closing = df[df["CLOSING STOCK(Ltr.)"] <= 2500]

# %%
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_opening, x="DATE AND TIME", y="OPENING STOCK(Ltr.)", hue="PRODUCT")
