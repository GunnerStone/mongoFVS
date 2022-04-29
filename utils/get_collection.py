import pymongo
from pymongo import MongoClient

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Configs.secrets import mongo_client_name
from Configs.secrets import mongo_client_database
from Configs.secrets import mongo_client_collection

# takes the FVS_Scans object and uploads it to the mongo database
def get_collection():
    client = MongoClient(mongo_client_name)
    db = client[mongo_client_database]
    collection = db[mongo_client_collection]
    return collection