from pymongo import MongoClient
import pandas as pd
import json


class MongoDBOperation:

    def __init__(self, client_url: str, database_name: str, collection_name: str = None):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name

    def create_client(self):
        client = MongoClient(self.client_url)
        return client

    def create_database(self):
        client = self.create_client()
        database = client[self.database_name]
        return database

    def create_collection(self, collection_name=None):
        database = self.create_database()

        if collection_name is None:
            collection_name = self.collection_name

        collection = database[collection_name]
        return collection

    def insert_record(self, record, collection_name=None):
        collection = self.create_collection(collection_name)

        if type(record) == list:
            for data in record:
                if type(data) != dict:
                    raise TypeError("record must be in dict format")

            collection.insert_many(record)

        elif type(record) == dict:
            collection.insert_one(record)

        else:
            raise TypeError("record must be dict or list of dicts")

    def bulk_insert(self, datafile: str, collection_name: str = None):
        if datafile.endswith(".csv"):
            data = pd.read_csv(datafile, encoding="utf-8")

        elif datafile.endswith(".xlsx"):
            data = pd.read_excel(datafile)

        else:
            raise ValueError("Only .csv and .xlsx files are supported")

        datajson = json.loads(data.to_json(orient="records"))

        collection = self.create_collection(collection_name)
        collection.insert_many(datajson)