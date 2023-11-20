import pandas as pd
import pymongo
#from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


class data_ingestion:
	"""
	This class will be used to ingest the data from the database


	"""

	def __init__(self,dataset_path):
		self.databasename = os.getenv('DATABASE_NAME')
		self.collection = os.getenv('COLLECTION_NAME')
		self.mongodbconnection = os.getenv("MONGODB_URL")
		self.directory_path = dataset_path
		self.input_data_path = f"{dataset_path}/InputFile.csv"

	def ingest_data_to_local(self):
		"""
		This method will be used to get the from the mongodb database

		"""
		try:
			client = pymongo.MongoClient(self.mongodbconnection)
			database = client[self.databasename]
			collection = database[self.collection]

			cursor = collection.find()

			list_cur = list(cursor)

			df = pd.DataFrame(list_cur)
			if not os.path.isdir(self.directory_path):
				os.mkdir(self.directory_path)

			df.to_csv(self.input_data_path)

		except Exception as e:
			raise e



b = data_ingestion(dataset_path = 'local')
b.ingest_data_to_local()
print(os.getcwd())
