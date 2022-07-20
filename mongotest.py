import pymongo
client = pymongo.MongoClient("mongodb+srv://ahertushar1:Bcmpa4228b#@cluster0.8qqmmk8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"tushar",
    "email" : "ahertushar1@gmail.com",
    "surname" : "aher"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )