def multiply_list():
    numList = input()
    numList = [int(x) for x in numList.splt()]    

    product = 1
    for i in numList:
        product = product * i
    return product

    for i in numList:
        if not i.isdigit():
            return bool(0)
