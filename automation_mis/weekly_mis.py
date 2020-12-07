import gspread
import pandas as pd
import os


#change currnet directory
os.chdir('C:\\Users\\panka\\github_repo\\Analytics\\automation_mis')

from methods import *


gc = gspread.service_account(filename='credential.json')
sh = gc.open_by_key('1c8GkIHjMkcmapbvEwDkBSQACzChlLROnfPXPlJJ8Txs')
data = sh.worksheet('data_transfer').get_all_values()

df = pd.DataFrame(data, columns=data[0])
df = df.drop([0])

cc_orpak = ['kumardeepak1@indianoil.in', 'grana@indianoil.in']
cc_atos= ['kumardeepak1@indianoil.in', 'grana@indianoil.in']
cc_hughes = ['kumardeepak1@indianoil.in', 'grana@indianoil.in', 'vpriyada@indianoil.in']
cc_nelco = ['kumardeepak1@indianoil.in', 'grana@indianoil.in', 'vpriyada@indianoil.in']

send_mail(create_html(df, "ATOS"), cc_atos, "ATOS")
