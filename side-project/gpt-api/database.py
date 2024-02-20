from dotenv import dotenv_values
from pymongo import MongoClient
import certifi

config = dotenv_values(".env")


class DBClient(MongoClient):
    def __init__(self):
        super().__init__(config["ATLAS_URL"], tlsCAFile=certifi.where())



def main():
    client = DBClient()
    production = client.production




if __name__ == "__main__":
    main()

