def listStringToInt(list):
    newList = []
    for item in list:
        if item.isnumeric():
            newList.append(int(item))
    return newList