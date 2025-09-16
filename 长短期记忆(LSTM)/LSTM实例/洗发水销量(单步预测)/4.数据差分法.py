from pandas import read_csv
from datetime import datetime
from pandas import Series

"""
差分序列就是用一个序列中，相邻两数进行相减
只考虑序列中的变化率，排除序列中所具有的趋势问题
"""
# 创建一个差分序列
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset.iloc[i] - dataset.iloc[i - interval]
		diff.append(value)
	return Series(diff)

# 还原差分序列
def inverse_difference(history, yhat, interval=1):
	return yhat + history.iloc[-interval]

# 数据格式处理
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('长短期记忆(LSTM)\LSTM实例\洗发水销量(单步预测)\shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, date_parser=parser)
print(series)
# 差分函数，差分步长为1
differenced = difference(series, 1)
print(differenced)
# invert transform
inverted = list()
for i in range(len(differenced)):
	value = inverse_difference(series, differenced[i], len(series)-i)
	inverted.append(value)

inverted = Series(inverted)
print(inverted)