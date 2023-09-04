# write a program to coonect to mongodb and add new collection and insert data into it
# and find data from collection and update data in collection and delete data from collection

import dotenv
from requests import request
from pymongo import MongoClient

db_list = request('GET', '')
print(db_list.text)


# # connect to mongodb
# client = MongoClient('localhost', 27017)

# # create database
# db = client['testdb']

# # create collection
# collection = db['testcollection']

# # insert data into collection
# collection.insert_one({'name': 'sachin', 'age': 24, 'city': 'bangalore'})
# collection.insert_one({'name': 'sachin', 'age': 24, 'city': 'bangalore'})

# # find data from collection
# data = collection.find()
# for i in data:
#     print(i)

# # update data in collection
# collection.update_one({'name': 'sachin'}, {'$set': {'name': 'sachin ramesh tendulkar'}})

# # delete data from collection
# collection.delete_one({'name': 'sachin ramesh tendulkar'})