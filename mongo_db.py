from ast import And
from pymongo import MongoClient
import pymongo

def get_database(data: any):
    #CONNECTION_STRING = "mongodb+srv://developer:qwerty123123@Project0.mongodb.net/myFirstDatabase"
    client = MongoClient()
    
    mydb = client["db"]
    
    mycol = mydb["data"]
    x = mycol.insert_one(data)

    print("Data inserted!")

if __name__ == "__main__":
    get_database()