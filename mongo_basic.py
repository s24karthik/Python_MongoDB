# All the MongoDB Workflow concepts and samples #
import json

# Main Intro selection block #
def mongo_base(client):
    print("""Enter the No. you want to perform the work task: 
                1. Create DB & collection 
                2. Insert Multi document """)
    val = int(input(" Enter the key: "))
    if val == 1:
        db, col = mongo_dbcreate(client)
    elif val == 2:
        document_insert(client)

# "MongoDB create database with collection"
def mongo_dbcreate(client):
    database, collection = input("Enter DB & collection name: \n").split()
    db = client[database]
    col = db[collection]
    return db, col


# "MongoDB create new document insertion"
def document_insert(client):
    db , col = mongo_dbcreate(client)
    insert_one = int(input("""  Inserting one or many document: 
                                1. Single document
                                2. Multi list document """))
    if insert_one == 1:
        with open("< YOUR LOCATION >") as file:
            file = json.load(file)
        result = col.insert_one(file)
        print("Mongo DB & Collection created")
        print("Successful insert:", result.inserted_id)
    else:
        with open("< YOUR LOCATION >") as file:
            file_data = json.load(file)     
        result = col.insert_many(file_data)
        print("Mongo DB & Collection created")
        print("Successful insert:", result.inserted_ids)
