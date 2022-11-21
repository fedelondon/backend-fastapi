def user_entity(term) -> dict:
    return {
        "name": str(term["name"]),
        "lastname": str(term["lastname"]),
        "identification": term["identification"],
    }


def users_entity(users) -> list:
    return [user_entity(term) for term in users]
