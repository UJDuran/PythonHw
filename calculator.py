def calculator(number1, number2, operator):
    operatorsList = ["+", "-", "*", "/", "//", "**"]

    if operator in operatorsList:
        if operator == operatorList[0]:
            return (number1 + number 2)
        elif operator == operatorList[1]:
            return (number1 - number2)
        elif operator == operatorList[2]:
            return (number1 * number2)
        elif operator == operatorList[3]:
            return (number1 / number2)
        elif operator == operatorList[4]:
            return (number1 //number2)
        elif operator == operatorList[5]:
            return (number1 ** number2)
    else:
        return bool(0)

def parse_input():
    eqString = input("Enter equation: ")
    eqList = eqString.split()

    num1 = int(eqList[0])
    num2 = int(eqList[2])
    operator = eqList[1]

    calculator(num1, num2, operator)
