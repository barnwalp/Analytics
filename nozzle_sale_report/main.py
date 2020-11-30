import pandas as pd
import os
from methods import *
from datetime import date, timedelta
import time
import pretty_errors


# change current directory
os.chdir('C:\\Users\\panka\\github_repo\\Analytics\\nozzle_sale_report')

from methods import *


# Read the downloaded excel file as df_1 and df_2
first_file = 'C:\\Users\\panka\\Downloads\\Nozzle Sales Report.xlsx'
second_file = 'C:\\Users\\panka\\Downloads\\Nozzle Sales Report (1).xlsx'
download_path = 'C:\\Users\\panka\\Downloads'

downloading_report(download_path)

df_1 = pd.read_excel(first_file)
df_2 = pd.read_excel(second_file)

day_1 = date.today() - timedelta(days=1)
day_2 = date.today() - timedelta(days=2)
day_3 = date.today() - timedelta(days=3)
day_4 = date.today() - timedelta(days=4)

pvt = pd.concat([
    create_pivot(df_2, day_3, day_4),
    create_pivot(df_1, day_1, day_2)
    ], axis=1)

pvt = pvt // 1000
pvt.loc["Grand-Total"] = pvt.sum()

send_mail(pvt.to_html(), first_file, second_file)
