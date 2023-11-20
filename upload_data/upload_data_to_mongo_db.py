import pymongo
#from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


class upload_data:
	"""
	This class will be used to upload the to mongo db database
	"""

	def __init__(self,dataset_path):
		self.databasename = os.getenv('DATABASE_NAME')
		self.collection = os.getenv('COLLECTION_NAME')
		self.mongodbconnection = os.getenv("MONGODB_URL")
		self.dataset_path = dataset_path


	def upload_data_to_mongodb(self):
		"""
			This method will be used to upload the data to mongo db database
		"""
		try:
			client = pymongo.MongoClient(self.mongodbconnection)
			database = client[self.databasename]
			collection = database[self.collection]
			collections_list = database.list_collection_names()

			if self.collection in collections_list:
				print(f"The collection {self.collection} already exists in {self.databasename}")

			else:
				df = pd.read_csv(self.dataset_path)

				return collection.insert_many(df.to_dict('records'))

		except Exception as e:
			raise e






a = upload_data(dataset_path = 'D:\FSDS\MAchine_Learning\Healthcare_project\healthcare_dataset.csv')
#a.upload_data_mongodb()










