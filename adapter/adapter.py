currency_rate = ['EUR', 'USD']


def data_adapter(data: list):
    x_rates_list = []
    data_dict = {}
    for item in data:
        date = item.get('date')
        rates = item.get('exchangeRate')
        value_dict = {}
        for value in rates:
            if value['currency'] in currency_rate:
                value_dict.update({value['currency']: {
                    'sale': round(value['saleRate'], 2),
                    'purchase': round(value['purchaseRate'], 2)
                }})
        data_dict.update({date: value_dict})
        x_rates_list.append({date: value_dict})
    return x_rates_list
