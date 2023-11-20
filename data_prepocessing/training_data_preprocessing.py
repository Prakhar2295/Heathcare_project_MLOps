import pandas as pd
import os
from data_validation.training_data_validation import data_validation
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

class data_preprocessing:
	"""
		This class will be used perform the preprocessing on the training dataset.

	"""
	def __init__(self,dataset):
		self.data_path = dataset
		self.validation  = data_validation()

	def feature_engineering(self):

		"""

				This method will perform the feature-engineering steps on the training dataset.

		"""
		try:
			self.df = pd.read_csv(self.data_path)
			self.df = pd.read_csv(self.data_path)
			self.df['Date of Admission'] = pd.to_datetime(self.df['Date of Admission'])
			self.df['Discharge Date'] = pd.to_datetime(self.df['Discharge Date'])
			self.df['duration_days'] = (self.df['Discharge Date'] - self.df['Date of Admission']).dt.days
			self.df['duration_days'] = self.df['duration_days'].astype(int)

			return self.df
		except Exception as e:
			raise e

	def remove_cols(self,cols_list:list):
		"""

			This method will be used to remove the columns.

		"""
		try:
			#self.cols_list = self.validation.cols_to_remove()
			self.cols_list = cols_list
			self.df = self.feature_engineering()

			if len(self.cols_list) > 0:
				self.df.drop(self.cols_list)
			else:
				print("No. cols to be dropped")
			return self.df

		except Exception as e:
			raise e


	def check_multicollinearity(self,dataframe):

		"""

				This method will be used to check the multicollinearity.

		"""
		try:
			self.cols_list_drop = []
			self.df = dataframe
			scaler = StandardScaler()
			arr = scaler.fit_transform(self.df)
			self.vif_df = pd.DataFrame()
			self.vif_df["vif"] = [variance_inflation_factor(arr, i) for i in range(arr.shape[1])]
			self.vif_df["features"] = self.df.columns
			for i,j in self.vif_df.iterrows():
				for p,q in j.items():
					if q > 5:
						self.cols_list.append(p)
			return self.cols_list_drop

		except Exception as e:
			raise e
























