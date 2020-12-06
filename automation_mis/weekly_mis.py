import gspread
import pandas as pd
import os

os.chdir('C:\\Users\\panka\\github_repo\\Analytics\\automation_mis')
gc = gspread.service_account(filename='credential.json')
sh = gc.open_by_key('1c8GkIHjMkcmapbvEwDkBSQACzChlLROnfPXPlJJ8Txs')
data = sh.worksheet('data_transfer').get_all_values()

df = pd.DataFrame(data, columns=data[0])
df = df.drop([0])


