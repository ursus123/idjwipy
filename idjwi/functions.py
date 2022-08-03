# Importing necessary libraries
import pandas as pd, os
from pandas_datareader.data import DataReader
from datetime import date

class open_data:

	def __init__(self, file_source, ticker,start_date, end_date):
		self.file_source = file_source
		self.ticker = ticker
		self.start_date = start_date
		self.end_date = end_date

	def open_csv_excel(self, file_source):
		"""
		This function is used to open csv and Excel files
		ursus
		:param file_source: is where you put your file path directory
		:type file_source: str

		:return: Dataframe
		:rtype: Dataframe
		"""
		try:
			file_name, file_extension = os.path.splitext(file_source)
			if file_extension =='.csv':
				data = pd.read_csv(file_source, header=True)
				return data
			elif file_extension =='.xlsx':
				data = pd.read_excel(file_source, header=True)
				return data
			else:
				print('Check Your Source')
		except FileNotFoundError:
			print('Check your file directory and try again')
	def open_stock_data(self, ticker,start_date,end_date):
		"""
		This is a function to open stock data
		:param ticker: this is where you put your ticker (str)
		:param start_date: this is where you put start date (YYY,M,D)(str)
		:param end_date: this is where you put start date (YYY,M,D)(str)
		:return: DataFrame
		:rtype: DataFrame
		"""
		start = date(int(start_date.split(',')[0]), int(start_date.split(',')[1]), int(start_date.split(',')[2]))
		end = date(int(end_date.split(',')[0]), int(end_date.split(',')[1]), int(end_date.split(',')[2]))
		data = DataReader(ticker, data_source='yahoo', start=start, end=end)
		return data


