import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,roc_auc_score,precision_score,f1_score
from data_transformation.data_transformation import data_transformation
from sklearn.model_selection import train_test_split


class model_training:
	"""
			This class will be used train the model.

	"""

	def __init__(self):
		self.data_transformation = data_transformation()

	def train_model(self):

		"""

				This method will train the model.


		"""
		self.X,self.y = self.data_transformation.data_scaling()

		self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(self.X,self.y,random_state = 120)

		xgb = XGBClassifier()






