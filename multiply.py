def multiply_list():
    print ("Enter a list of numbers seperated by a space")
    numList = [int(x) for x in input().split()]

    product = 1
    isNum = bool(1)


    for i in numList:
        if type(i) == int or type(i) == float:
            product = product * i
        else:
            return bool(0)

    return product
