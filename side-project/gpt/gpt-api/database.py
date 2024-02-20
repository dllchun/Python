from dotenv import dotenv_values
from pymongo import MongoClient
import certifi

config = dotenv_values(".env")


class DBClient(MongoClient):
    def __init__(self):
        super().__init__(config["ATLAS_URL"], tlsCAFile=certifi.where())

    def insert_one(self, collection, docs: dict):
        inserted_id = self[collection].insert_one(docs).inserted_id
        return inserted_id


