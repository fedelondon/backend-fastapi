from fastapi import APIRouter

from config.db import conn
from models.userModel import User
from schemas.userSchema import user_entity, users_entity

user = APIRouter()


@user.get("/user")
async def find_all_users():
    return users_entity(conn.prueba.user.find())


@user.get("/user/{:id}")
async def find_user():
    return {"message": "Hello user"}


@user.post("/user")
async def create_user(user: User):
    new_user = dict(user)
    new_user["name"] = new_user["name"].upper()
    new_user["lastname"] = new_user["lastname"].upper()
    user_inserted = conn.prueba.user.insert_one(new_user).inserted_id
    return str(user_inserted)


@user.patch("/user/{id}")
async def update_user():
    return {"message": "Hello user"}


@user.delete("/user/{id}")
async def delete_user():
    return {"message": "Hello user"}
