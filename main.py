import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["CRUD_operations"]
mycol = mydb["CRUD"]
myquery = {"last_name":"Marrier"}
newvalues={"$set":{"last_name":"Williomson"}}

#for Updating
mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)