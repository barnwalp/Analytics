import pandas as pd

def clean_data(df, day_1, day_2):
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

    # Deleting 1st row; indexing start from 0
    df = df.drop(df.index[0])

    df = df.rename(columns={
        'Issue Sales': self.day_1,
        'Unnamed: 19': self.day_2
        })

    df = df[
            (df['Product'] == 'XP') |
            (df['Product'] == 'MS') |
            (df['Product'] == 'HSD')
            ]
    pvt_table = pd.pivot_table(
            df,
            index=["SA"],
            columns=["Proudct"],
            values=[day_1, day_2],
            aggfunc=sum)

    return pvt_table


