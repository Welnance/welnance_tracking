
def socialEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "Facebook": item["Facebook"],
        "Twitter": item ["Twitter"],
        "CMC": item ["CMC"]
    }

def socialsEntity(entity) -> list:
    return [socialEntity(item) for item in entity]


def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]