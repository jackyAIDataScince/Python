import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# This will show database 
mydb = myclient["mydatabase"]

print(mydb)
print(myclient)
# this will show collection
mycol = mydb["customers"]

print(mycol)
