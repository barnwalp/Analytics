def create_pivot(df, day_1, day_2):
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
    df = df.drop(df.index[1])

    df = df.rename(columns={
        'Issue Sales': day_1,
        'Unnamed: 19': day_2
        })

    # filter out Proudct column
    df = df[
            (df['Product'] == 'XP') |
            (df['Product'] == 'MS') |
            (df['Product'] == 'HS')
            ]

    # Replace XP with MS in Product column
    df.loc[df['Product'] == 'XP', 'Product'] = 'MS'

    pvt_table = pd.pivot_table(
            df,
            index=["SA"],
            columns=["Product"],
            values=[day_1, day_2],
            aggfunc=sum)

    return pvt_table
