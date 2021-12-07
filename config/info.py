import base64
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admindb:lTTNm2B0wCfZsFDh@cluster0.zlh0s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".encode("utf-8"))

db = client.social_data.encode("utf-8")

collection_name = db ["socials"]