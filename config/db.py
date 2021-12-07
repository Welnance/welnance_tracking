from pymongo import MongoClient
import base64

client = MongoClient("mongodb+srv://admindb:lTTNm2B0wCfZsFDh@cluster0.zlh0s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.social_data

collection_name = db ["socials"]