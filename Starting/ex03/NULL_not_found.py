def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is float and object == float("NaN"):
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif type(object) is str and object == "":
        print(f"Empty: {type(object)}")
    elif type(object) is bool and object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0