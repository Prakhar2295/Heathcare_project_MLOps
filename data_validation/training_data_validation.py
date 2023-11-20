import pandas as pd
import os



class data_validation:
	"""
	This class will be used to validate the data
	"""

	def __init__(self,datapath):
		self.data_path = datapath


	def cols_to_remove(self):

		"""
		This method will be used to check for the columns if they are having any
		columns with 0 standard deviation.


		"""

		df = pd.read_csv(self.data_path)
		df_des = df.describe()

		self.col_to_remove = []

		try:
			for rows, cols in df_des.iterrows():
				for col_name, vals in cols.items():
					if rows == df_des.index[2]:
						if vals == 0:
							self.col_to_remove.append(col_name)
						else:
							print("NO cols found")

			return self.col_to_remove
		except Exception as e:
			raise e







