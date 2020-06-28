from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

start_date = '2010-06-01'
end_date = '2020-06-20'

stock_data = data.DataReader('PFE', 'yahoo', start_date, end_date)
print(stock_data)
# print(list(stock_data.index))


'''
{"2020-01-02T00:00:00.000Z":38.3619155884,
    "2020-01-03T00:00:00.000Z":38.1560897827,
    "2020-01-06T00:00:00.000Z":38.1070823669,
    "2020-01-07T00:00:00.000Z":37.9796714783,...,
    "2020-06-19T00:00:00.000Z":33.4199981689
}
'''
# print(stock_data['Adj Close'].to_json(orient="index", date_format='iso'))

print(stock_data.to_json(orient="index", date_format='iso'))