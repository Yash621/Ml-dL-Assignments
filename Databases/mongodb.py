from typing import Collection
import pymongo as go
client = go.MongoClient(
    "mongodb+srv://yash:yash@cluster0.hiudc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
print(client.list_database_names())
db1 = client["jadoo"]
print(client.list_database_names())
Collection = db1["test"]
record = {
    "jhdj": "jkdjf",
    "jdkff": "dfjkf"
}
Collection.insert_one(record)
