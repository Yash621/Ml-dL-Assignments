import pymongo as go
client = go.MongoClient(
    "mongodb+srv://yash:yash@cluster0.hiudc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
print(client.list_database_names())
