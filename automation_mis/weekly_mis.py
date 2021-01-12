import gspread
import pandas as pd
import os


#file_path = os.path.join(os.getcwd(), 'Analytics', 'automation_mis')
#change currnet directory
#os.chdir(file_path)

from methods import *
from whatsapp import *


gc = gspread.service_account(filename='credential.json')
sh = gc.open_by_key('1c8GkIHjMkcmapbvEwDkBSQACzChlLROnfPXPlJJ8Txs')
data = sh.worksheet('data_transfer').get_all_values()

df = pd.DataFrame(data, columns=data[0])
df = df.drop([0])

to_atos = ['chinmay.atos@yahoo.com', 'chinmay.kumar@atosra.net', 'manojkumar.atos@gmail.com', 'manojkumar.behera@atosra.net']
to_orpak = ['Jayanta.Pati@gilbarco.com', 'ssahu3990@gmail.com']
to_hughes = ['shahbaz.alam@os.hughes.in']
to_nelco = ['ioclbhubaneswar@nelco.in']

cc_orpak = ['kumardeepak1@indianoil.in', 'grana@indianoil.in', 'mishrank@indianoil.in', 'biswanathbadi@gmail.com']
cc_atos= ['kumardeepak1@indianoil.in', 'grana@indianoil.in', 'mishrank@indianoil.in', 'biswanathbadi@gmail.com']
cc_hughes = ['kumardeepak1@indianoil.in', 'grana@indianoil.in', 'vpriyada@indianoil.in', 'mishrank@indianoil.in', 'biswanathbadi@gmail.com', 'Jayanta.Pati@gilbarco.com', 'ssahu3990@gmail.com', 'chinmay.atos@yahoo.com', 'manojkumar.atos@gmail.com']
cc_nelco = ['kumardeepak1@indianoil.in', 'grana@indianoil.in', 'vpriyada@indianoil.in', 'mishrank@indianoil.in', 'biswanathbadi@gmail.com', 'Jayanta.Pati@gilbarco.com', 'ssahu3990@gmail.com', 'chinmay.atos@yahoo.com', 'manojkumar.atos@gmail.com']

send_mail(create_html(df, "ATOS"), to_atos, cc_atos, "ATOS")
send_mail(create_html(df, "ORPAK"), to_orpak, cc_orpak, "ORPAK")
send_mail(create_html(df, "HUGHES"), to_hughes, cc_hughes, "HUGHES")
send_mail(create_html(df, "NELCO"), to_nelco, cc_nelco, "NELCO")

"""
df = df[df['Dependency'] == "IOCL"]
df = df[['RO Name', 'Reason for non-transfer of data']]
data = df.values.tolist()

for values in data:
    str = '- '.join(values)
    print(send_whatsapp(str, 9437086233))

"""
