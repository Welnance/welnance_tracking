from fastapi import APIRouter
from models.socials import Socials
from config.db import db
from schemas.socials import serializeDict, serializeList
from bson import ObjectId


socials = APIRouter()


@socials.get('/')
async def Get_social_data():
    return serializeList(db.socials.find())

@socials.post('/')
async def post_social(socials: Socials):
    db.socials.insert_one(dict(socials))
    return serializeList(db.socials.find())

@socials.put('/{id}')
async def update_socials(id,socials: Socials):
    db.socials.find_one_and_update({"_id":ObjectId(id)},
    {
        "$set":dict(socials)
    })
    return serializeDict(db.socials.find_one({"_id":ObjectId(id)}))
@socials.delete('/{id}')
async def delete_submission(id):
    return serializeDict(db.socials.find_one_and_delete({"_id":ObjectId(id)}))        