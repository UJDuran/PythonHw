def multiply_list():
    print ("Enter a list of numbers seperated by a space")
    numList = [int(x) for x in input().split()]

    product = 1
    isNum = bool(1)


    for i in numList:
        product = product * i
        if i == 0:
            return bool(0)
