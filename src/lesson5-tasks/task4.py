import random

dimSize = 20
xBound = 1
yBound = 11
dim = [random.randint(xBound, yBound) * (-1)**i for i in range(dimSize)]

checkNumberStr = input('Please enter the number in range from {0} to {1} to check: '.format(xBound, yBound))
try:
    checkNumber = int(checkNumberStr)
    checkResult = dim.count(checkNumber)
    print('Array generated: \n', dim)
    print('Number {0} is repeated in array {1} time(s)'.format(checkNumber, checkResult))
except Exception as e:
    print(e)
