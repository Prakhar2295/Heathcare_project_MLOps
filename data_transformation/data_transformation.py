import pandas as pd
from data_prepocessing.training_data_preprocessing import data_preprocessing
import category_encoders as ce
from sklearn.preprocessing import LabelEncoder as lb
from sklearn.preprocessing import StandardScaler

class data_transformation:
	"""

			This class will be used to perform the data transformation
			on the training dataset.

	"""

	def __init__(self):
		self.preprocessing = data_preprocessing()


	def data_transformation(self):
		"""

				This method will data transformation on the dataset.

		"""
		try:

			self.cols_to_drop = ['Name','Hospital','Room Number','Doctor']

			self.df = self.preprocessing.remove_cols(self.cols_to_drop)

			self.cols_list_drop =self.preprocessing.check_multicollinearity(self.df)

			self.df = self.preprocessing.remove_cols(self.cols_list_drop)

			self.X = self.df.iloc[:, list(range(1,8)) + [9]]   ###Spliting the data into features and targets

			self.y = self.df.iloc[:,8]

			return self.X,self.y

		except Exception as e:
			raise e



	def data_encoding(self):

		"""

				This method will be used to encode the categorical feature and targets
				into numerical setup.

		"""
		try:
			self.X,self.y = data_transformation()
			self.y = lb.fit_transform(self.y)
			cat_enc = ce.TargetEncoder(smoothing=0)
			self.X = cat_enc.fit_transform(self.X,self.y)

			self.cols_drop = self.preprocessing.check_multicollinearity(self.X)

			self.X = self.preprocessing.remove_cols(self.cols_drop)


			return self.X,self.y

		except Exception as e:
			raise e


	def data_scaling(self):

		"""
				This method will scale the data.


		"""
		try:
			self.X,self.y = self.data_encoding()

			self.scaler = StandardScaler()

			self.X = self.scaler.fit_transform(self.X)

			return self.X,self.y

		except Exception as e:
			raise e



































