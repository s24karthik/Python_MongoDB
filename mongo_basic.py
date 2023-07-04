# All the MongoDB Workflow concepts and samples #
import json
import pandas as pd

# Main Intro selection block #
def mongo_base(client):
    print("""Enter the No. you want to perform the work task: 
                1. Insert Document
                2. Export Document""")
    val = int(input(" Enter the key: "))
    if val == 1:
        document_insert(client)
    elif val == 2:
        mongo_export(client)
        
# MongoDB create database with collection #
def mongo_dbcreate(client):
    database, collection = input("Enter DB & collection name: \n").split()
    db = client[database]
    col = db[collection]
    return db, col

# MongoDB create new document insertion #
def document_insert(client):
    db, col = mongo_dbcreate(client)
    insert_one = int(input("""  Inserting one or many document: 
                                1. Single document
                                2. Multi list document """))
    if insert_one == 1:
        with open("< FILE PATH >") as file:
            file = json.load(file)
        result = col.insert_one(file)
        print("Mongo DB & Collection created")
        print("Successful document insert:", result.inserted_id)
    else:
        with open("< FILE PATH >") as file:
            file_data = json.load(file)     
        result = col.insert_many(file_data)
        print("Mongo DB & Collection created")
        print("Successful document insert:", result.inserted_ids)

# MongoDB data export #
def mongo_export(client):
    db = client.get_database(input("Enter your DB: "))
    col = db.get_collection(input("Enter your collection: "))
    query = json.loads(input("Enter your query: "))
    res = col.find_one(query)
    df = pd.DataFrame(res)
    df.to_csv(path_or_buf="< FILE PATH >")