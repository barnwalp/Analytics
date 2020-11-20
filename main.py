import pandas as pd
import os
from methods import *
from datetime import date, timedelta
import time
import pretty_errors

# Read the downloaded excel file as df_1 and df_2
first_file = 'C:\\Users\\panka\\Downloads\\Nozzle Sales Report.xlsx'
second_file = 'C:\\Users\\panka\\Downloads\\Nozzle Sales Report (1).xlsx'

print(first_file)

df_1 = pd.read_excel(first_file)
df_2 = pd.read_excel(second_file)

day_1 = date.today() - timedelta(days=1)
day_2 = date.today() - timedelta(days=2)
day_3 = date.today() - timedelta(days=3)
day_4 = date.today() - timedelta(days=4)

# print(clean_data(df_1, day_1, day_2))
pvt = pd.concat([
    create_pivot(df_1, day_1, day_2),
    create_pivot(df_2, day_3, day_4)
    ], axis=1)

print(pvt)
