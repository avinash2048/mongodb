import pandas as pd 
from sqlalchemy import create_engine 

# load data
engine=create_engine("postgresql://postgres:Orange1$#@localhost:5432/Train")
data= pd.read_sql("Train",engine)  #  via table name
# data=pd.read_sql('select * from "Train" where "Survived"=1',engine)  #via query
print(data.head())
print(f"{len(data)}survived records retrieved from postgresql")