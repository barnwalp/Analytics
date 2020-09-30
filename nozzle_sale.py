import numpy as np
import pandas as pd
import os

path = 'C:/Users/panka/Downloads/Nozzle Sales Report.xlsx'
df = pd.read_excel(path)

df = df.drop(columns=[
    'RO Market Type',
    'SO',
    'SO Code',
    'DO', 'DO Code',
    'SA Code',
    'Phase',
    'SAT Status',
    'VSAT Installation',
    'Control Record Reconcilation',
    'Unnamed: 15',
    'Transaction Stock Reconcilation',
    'Unnamed: 17',
    'Totalizer Sales',
    'Unnamed: 21',
    'Total Transaction Sales',
    'Total Totalizer Sales',
    'Average Issue Sales',
    'Average Totalizer Sales',
    'Percentage Difference',
    'RO Eligible'
    ])

df = df.drop(df.index[0])

df = df.rename(columns={
    'Issue Sales': '28-09-2020',
    'Unnamed: 19': '29-09-2020'
    })
