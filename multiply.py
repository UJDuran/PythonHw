def multiply_list():
    numList = input()
    

    product = 1
    for i in numList:
        if i.isdigit:
            product = product * i
    return product

    for i in numList:
        if not i.isdigit():
            return bool(0)
