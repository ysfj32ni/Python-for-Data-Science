def all_thing_is_obj(object: any) -> int:
    objectType = type(object)
    if objectType is str:
        print(f"{object} is in the kitchen : {objectType}")
    elif objectType is list:
        print(f"List : {type(object)}")
    elif objectType is dict:
        print(f"Dict : {type(object)}")
    elif objectType is tuple:
        print(f"Tuple : {type(object)}")
    elif objectType is set:
        print(f"Set : {type(object)}")
    else:
        print("Type not found")
    return 42
