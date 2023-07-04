# Python codebase snippets for various GCP Biqguery services #
import pandas as pd
import mongo_basic
from pymongo import MongoClient

# Snippet to get connected to MongoDB #
url = input("Enter the MongoDB URL: ")
client = MongoClient(url)
result = client.server_info
print("Connect stats: ", result)

# Function to trigger all the different MongoDB workflows and sample codebases #
def mongo_workflow():
    #**  Basic Mongo operations **#
    mongo_basic.mongo_base(client)

mongo_workflow()