import pandas as pd
from pymongo import MongoClient
import json
#client =MongoClient('localhost',27017)
client=MongoClient('mongodb://localhost:27017')
# read data 
db=client.titanic_db
train=db.train
data=train.find({"Survived":1})
for val in data :
    print(val)
print(f"{data.retrieved} survived records retrieved from mongodb")
