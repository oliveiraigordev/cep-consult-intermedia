from dataclasses import dataclass
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.collection import Collection
from pymongo.database import Database
from os import environ
from typing import Any, Dict


load_dotenv()

CONNECTION_STRING: str = environ.get('MONGODB_URI')
DATABASE: str = environ.get('MONGODB_DATABASE')


@dataclass
class DatabaseQuery:
    client: MongoClient = MongoClient(
        CONNECTION_STRING,
        server_api=ServerApi('1')
        )
    database: Database = client[DATABASE]

    def handle_collection(self, collection: Collection) -> Collection:
        return self.database[collection]

    def query_find_one(self,
                       collection: Collection,
                       json: Dict
                       ) -> Dict[str, Any] | None:
        result = collection.find_one(json)
        return result
