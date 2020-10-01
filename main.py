import pandas as pd
# import os
from nozzle_sale import *
from datetime import date, timedelta
import time

# Read the downloaded excel file as df_1 and df_2
first_file = 'C:/Users/panka/Downloads/Nozzle Sales Report.xlsx'
second_file = 'C:/Users/panka/Downloads/Nozzle Sales Report (1).xlsx'

df_1 = pd.read_excel(first_file)
df_2 = pd.read_excel(second_file)

day_1 = date.today() - timedelta(days=1)
day_2 = date.today() - timedelta(days=2)
day_3 = date.today() - timedelta(days=3)
day_4 = date.today() - timedelta(days=4)

print(clean_data(df_1, day_1, day_2))
