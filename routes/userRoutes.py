from fastapi import APIRouter, HTTPException
from bson import ObjectId
from config.db import conn
from models.userModel import User
from schemas.userSchema import user_entity, users_entity

user = APIRouter()


@user.get("/user")
async def find_all_users():
    return users_entity(conn.prueba.user.find())


@user.get("/user/{id}")
async def find_user(id: str):
    return user_entity(conn.prueba.user.find_one({"_id": ObjectId(id)}))



@user.post("/user")
async def create_user(user: User):
    new_user = dict(user)
    del new_user["id"] 
    new_user["name"] = new_user["name"].upper()
    new_user["lastname"] = new_user["lastname"].upper()
    ident = new_user['identification']
    identdb = conn.prueba.user.find_one({"identification": ident})
    if(user_entity(identdb)):
        raise HTTPException(status_code=400, detail="Dupicate identification")
    user_inserted = conn.prueba.user.insert_one(new_user).inserted_id
    inseted_user = conn.prueba.user.find_one({"_id": user_inserted})
    return user_entity(inseted_user)


@user.patch("/user/{id}")
async def update_user():
    return {"message": "Hello user"}


@user.delete("/user/{id}")
async def delete_user():
    return {"message": "Hello user"}
