import pymongo

mongo_client = pymongo.MongoClient(host="mongodb://localhost:27017/")
db_name = "jag_db"
collection_name = "jag_collection"

if db_name in mongo_client.list_database_names():
    database_handle = mongo_client[db_name]
    print('Database found!')
    if collection_name in database_handle.list_collection_names():
        print('Collection Found')
        collection_handle = database_handle[collection_name]
        print(collection_handle)
    else:
        print('Collection not found')
else:
    print('Data base not found')

