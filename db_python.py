# write a program to coonect to mongodb and add new collection and insert data into it
# and find data from collection and update data in collection and delete data from collection

import os
from dotenv import load_dotenv

from requests import request
from pymongo import MongoClient

import json

load_dotenv()



def drop_database(client, db_name):
    client.drop_database(db_name)


def create_new_collection(collection):
    # insert data into collection
    collection.insert_one({'name': 'tmp'})
    
    # delete data from collection
    collection.delete_one({'name': 'tmp'})


def add_new_users_to_collection(client, start_index):
        # connect to database
        db = client["user_db"]
        

        for i in range(start_index, start_index+10):
            collection_name = "user" + str(i).zfill(5)
            create_new_collection(db[collection_name])
        
        collection_names_list = db.list_collection_names()
        collection_names_list = sorted(collection_names_list)
        print(f"{collection_names_list = }")
        # print(json.dumps(collection_names_list, indent=4))


def main():
    db_list_url = os.getenv('DB_LIST_URL')

    db_list = request("GET", db_list_url).json()
    # print(json.dumps(db_list, indent=4, sort_keys=True))

    for db_index, db_url in enumerate(db_list, start=1):
        db_url = db_list[0]["db"]

        # connect to mongodb cluster
        client = MongoClient(db_url)

        # list all databases
        db_names_list = client.list_database_names()
        final_db_names_list = list(set(db_names_list) - set(['admin', 'config', 'local']))

        if("user_db" in final_db_names_list):
            drop_database(client=client, db_name="user_db")
        
        add_new_users_to_collection(client=client, start_index=((db_index-1)*10)+1)


if __name__ == "__main__":
    main()