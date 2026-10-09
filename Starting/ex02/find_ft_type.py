def all_thing_is_obj(object: any) -> int:
    objectType = type(object)
    if objectType is str:
        print(f"{object} is in the kitchen : {objectType}")
    elif objectType is int:
        print("Type not found")
    else:
        print(f"{object.__class__.__name__} : {type(object)}")
    return 42