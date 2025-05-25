def revenue_share(owner_share, rtkm, tt_capacity, no_of_trip):
    tt_details = {
        22: {
            'rtkm_rate': 2.44,
            'mileage': 3.5,
            'emi_7_monthly': 53444.8,
            'driver_helper_salary': 25000,
            'annual_tt_insurance': 60000,
            'annual_product_insurance': 9000,
            'annual_road_tax': 26000,
            'annual_road_permit': 4000,
            'tyre_yearly_cost': 150000,
            'lub_spare_yearly_cost': 35000,
            'toll_per_trip': 492,
            'per_trip_expense': 300,
            'per_trip_fooding': 1500
        },
        14: {
            'rtkm_rate': 2.85,
            'mileage': 5.5,
            'emi_7_monthly': 42004,
            'driver_helper_salary': 25000,
            'annual_tt_insurance': 60000,
            'annual_product_insurance': 9000,
            'annual_road_tax': 18000,
            'annual_road_permit': 4000,
            'tyre_yearly_cost': 90000,
            'lub_spare_yearly_cost': 25000,
            'toll_per_trip': 380,
            'per_trip_expense': 300,
            'per_trip_fooding': 1500
        },
    }
    tt_dict = tt_details[tt_capacity]
    revenue_per_month = rtkm * tt_capacity * tt_dict['rtkm_rate'] * no_of_trip

    per_trip_expense = per_trip_cost(rtkm, tt_capacity, no_of_trip, owner_share)
    fixed_monthly_expense = fixed_cost(tt_capacity)

    net_profit = revenue_per_month - fixed_monthly_expense - per_trip_expense
    own_profit = net_profit * 0.4
    percentage_share = own_profit / revenue_per_month
    # print(f'{revenue_per_month} --> {fixed_monthly_expense} --> {per_trip_expense}')
    return net_profit, own_profit, percentage_share


def fixed_cost(tt_capacity):
    tt_details = {
        22: {
            'rtkm_rate': 2.44,
            'mileage': 3.5,
            'emi_7_monthly': 53444.8,
            'driver_helper_salary': 25000,
            'annual_tt_insurance': 60000,
            'annual_product_insurance': 9000,
            'annual_road_tax': 26000,
            'annual_road_permit': 4000,
            'tyre_yearly_cost': 150000,
            'lub_spare_yearly_cost': 35000,
            'toll_per_trip': 492,
            'per_trip_expense': 300,
            'per_trip_fooding': 1500
        },
        14: {
            'rtkm_rate': 2.85,
            'mileage': 5.5,
            'emi_7_monthly': 42004,
            'driver_helper_salary': 25000,
            'annual_tt_insurance': 60000,
            'annual_product_insurance': 9000,
            'annual_road_tax': 18000,
            'annual_road_permit': 4000,
            'tyre_yearly_cost': 90000,
            'lub_spare_yearly_cost': 25000,
            'toll_per_trip': 380,
            'per_trip_expense': 300,
            'per_trip_fooding': 1500
        },
    }
    tt_dict = tt_details[tt_capacity]
    fixed_monthly_expense = tt_dict['emi_7_monthly'] + ((tt_dict['driver_helper_salary']*12 + tt_dict['annual_tt_insurance'] + tt_dict['annual_product_insurance'] + tt_dict['annual_road_tax'] + tt_dict['annual_road_permit'] + tt_dict['tyre_yearly_cost'] + tt_dict['lub_spare_yearly_cost']) / 12)
    return fixed_monthly_expense


def per_trip_cost(rtkm, tt_capacity, no_of_trip, owner_share):
    hsd_rate = 88.69
    tt_details = {
        22: {
            'rtkm_rate': 2.44,
            'mileage': 3.5,
            'emi_7_monthly': 53444.8,
            'driver_helper_salary': 25000,
            'annual_tt_insurance': 60000,
            'annual_product_insurance': 9000,
            'annual_road_tax': 26000,
            'annual_road_permit': 4000,
            'tyre_yearly_cost': 150000,
            'lub_spare_yearly_cost': 35000,
            'toll_per_trip': 492,
            'per_trip_expense': 300,
            'per_trip_fooding': 1500
        },
        14: {
            'rtkm_rate': 2.85,
            'mileage': 5.5,
            'emi_7_monthly': 42004,
            'driver_helper_salary': 25000,
            'annual_tt_insurance': 60000,
            'annual_product_insurance': 9000,
            'annual_road_tax': 18000,
            'annual_road_permit': 4000,
            'tyre_yearly_cost': 90000,
            'lub_spare_yearly_cost': 25000,
            'toll_per_trip': 380,
            'per_trip_expense': 300,
            'per_trip_fooding': 1500
        },
    }
    tt_dict = tt_details[tt_capacity]

    revenue_per_month = rtkm * tt_capacity * tt_dict['rtkm_rate'] * no_of_trip
    tds = revenue_per_month * 0.02
    owner_value = revenue_per_month * owner_share

    fuel_cost = (rtkm/tt_dict['mileage']) * hsd_rate
    trip_expense = (tt_dict['toll_per_trip'] + tt_dict['per_trip_expense'] + tt_dict['per_trip_fooding'] + fuel_cost) * no_of_trip + tds + owner_value
    return trip_expense


if __name__ == '__main__':
    print('owner share is 8%')
    print(revenue_share(0.08, 1100, 22, 8)[0])
    print('owner share is 0%')
    print(revenue_share(0.05, 916, 14, 7)[1])
