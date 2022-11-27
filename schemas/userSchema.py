def user_entity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": str(user["name"]),
        "lastname": str(user["lastname"]),
        "identification": int(user["identification"]),
    }


def users_entity(users) -> list:
    return [user_entity(term) for term in users]
