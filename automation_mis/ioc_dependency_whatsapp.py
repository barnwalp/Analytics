import gspread
import pandas as pd
import os


#change currnet directory
os.chdir('C:\\Users\\panka\\github_repo\\Analytics\\automation_mis')

from methods import *
from whatsapp import *

gc = gspread.service_account(filename='credential.json')
sh = gc.open_by_key('1c8GkIHjMkcmapbvEwDkBSQACzChlLROnfPXPlJJ8Txs')
data = sh.worksheet('data_transfer').get_all_values()

df = pd.DataFrame(data, columns=data[0])
df = df.drop([0])

df = df[df['Dependency'] == "IOCL"]
df = df[['RO Name', 'Reason for non-transfer of data']]
data = df.values.tolist()
print(data)

for values in data:
    str = '- '.join(values)
    print(send_whatsapp(str, 9437086233))


