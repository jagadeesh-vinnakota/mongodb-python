import pymongo


def database_connection(host, database_name):
    mongo_client = pymongo.MongoClient(host=host)
    if database_name in mongo_client.list_database_names():
        return mongo_client[database_name]
    else:
        return Exception("Data Base Not found!")


def collection_connection(database_handle, collection_name):
    if collection_name in database_handle.list_collection_names():
        return database_handle[collection_name]
    else:
        return Exception("Collection not found!")


def single_insert(collection_handle, data):
    return collection_handle.insert_one(data)


def multiple_insert(collection_handle, data):
    return collection_handle.insert_many(data)


def single_retrieval(collection_handle):
    return collection_handle.find_one()


def multiple_retrieval(collection_handle, filter = {}):
    return col_handle.find(filter)


if __name__== "__main__":
    db_handle = database_connection(host="mongodb://localhost:27017/", database_name="jag_db")
    db_flag = not isinstance(db_handle, Exception)

    if db_flag:
        col_handle = collection_connection(db_handle, "jag_collection")

    col_flag = not isinstance(col_handle, Exception)
    data = {"key": "value",
            "likes": 95}

    multi_data = [{
        "name": "jagadeesh",
        "likes": 200
    },
        {
            "name": "vinnakota",
            "likes": 150
        }]
    if db_flag and col_flag:
        insert_handle = single_insert(col_handle, data)
        print(insert_handle.inserted_id)

        multi_insert_handle = multiple_insert(col_handle, multi_data)
        print(multi_insert_handle.inserted_ids)

    if db_flag and col_flag:
        print(single_retrieval(col_handle))
        for data in multiple_retrieval(col_handle, {"likes": {"$gt": 55}}):
            print(data)