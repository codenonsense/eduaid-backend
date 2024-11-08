from config import MONGO_URI
from pymongo import MongoClient

def mongo_connect():
    client = MongoClient(MONGO_URI)
    db = client['EduAid']
    print('_____________________________')
    print('\n')
    print('MongoDB is Connected')
    print('\n')
    print('-----------------------------')
    return db 
