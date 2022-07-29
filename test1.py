import pymongo

client = pymongo.MongoClient("mongodb+srv://kirankhera5:Kiran1234@kkcluster.teqei.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "name" : "sudhanshu",
    "mail_id" : "sudhanshu@inueron.ai",
    "subject" : ["daa science", "big data","data analysitcs"]
}

database = client['myinfo']
collection = database["sudh"]
collection.insert_one(data)
