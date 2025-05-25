import pandas as pd
from transport_methods import per_trip_cost
from transport_methods import fixed_cost
import os
from openpyxl import load_workbook


os.chdir('D:\\Personal\\Reports')
# print(os.listdir())
df = pd.read_excel('Transport Calculation.xlsx', sheet_name='Vehicle')

vehicle_dict = df[['Vehicle Number', 'TT Details']].set_index('Vehicle Number').T.to_dict('list')
# we can remove nan key in dictionary by simple list comprehension based on
# on the fact that nan does not equal itself
vehicle_dict = {k: v for k, v in vehicle_dict.items() if k == k}

trip_dict = df[['Unique Id', 'Vehicle Number', 'RO Name', 'Owners Share', 'RTKM', 'TT Details', 'No of Trip']].set_index('Unique Id').T.to_dict('list')
vehicle_data = {14: [2.85], 22: [2.44]}

for key, value in vehicle_data.items():
    monthly_fixed_cost = fixed_cost(key)
    vehicle_data[key].append(monthly_fixed_cost)

for key, value in trip_dict.items():
    per_trip_expense = per_trip_cost(value[3], value[4], value[5], value[2])
    revenue_per_month = value[3] * value[4] * vehicle_data[value[4]][0] * value[5]
    trip_dict[key].append((revenue_per_month))
    trip_dict[key].append(per_trip_expense)

for key1, value1 in vehicle_dict.items():
    profit = 0
    for key2, value2 in trip_dict.items():
        if value2[0] == key1:
            profit = profit + value2[-2] - value2[-1]
    profit = profit - vehicle_data[value1[0]][1]
    vehicle_dict[key1].append(profit)

df_dict = pd.DataFrame.from_dict(vehicle_dict, orient='index')
df_trip = pd.DataFrame.from_dict(trip_dict, orient='index')

with pd.ExcelWriter('Transport Calculation.xlsx', engine='openpyxl') as writer:
    writer.book = load_workbook('Transport Calculation.xlsx')
    df_dict.to_excel(writer, index=True)

with pd.ExcelWriter('Transport Calculation.xlsx', engine='openpyxl') as writer:
    writer.book = load_workbook('Transport Calculation.xlsx')
    df_trip.to_excel(writer, index=True)
