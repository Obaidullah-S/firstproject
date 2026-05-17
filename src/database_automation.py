from mongoDBconnect.mongo_crud import MongoDBOperation


class mongo_operation(MongoDBOperation):

    def __init__(self, client_url, database_name, collection_name):
        super().__init__(client_url, database_name, collection_name)