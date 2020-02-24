import pandas as pd
from pymongo import MongoClient
import json
#client =MongoClient('localhost',27017)

client=MongoClient('mongodb://localhost:27017')
#extrat data
data=pd.read_csv("input/train.csv")
data["test"]=json.dumps({"key1":"value1","key2":"value2"})
data["test"]=data["test"].apply(lambda x: json.loads(x))

# transform data
my_data=data.to_dict(orient="records")
#my_data=json.dumpos(my_data)
print(my_data[:2])  #print top 2 rows onlu
# load data 
db=client.titanic_db
train=db.train
result=train.insert_many(my_data)
print(f"Multiple posts:{len(result.inserted_ids)}")
