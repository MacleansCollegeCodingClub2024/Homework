def getEven(x):
    Even = []
    for n in x:
        if not n %2:
            Even.append(n)
    return Even

numbers = [2,3,4,6,8,101,103,111,120,124]

print(getEven(numbers))
