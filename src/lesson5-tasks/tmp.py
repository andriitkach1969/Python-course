numStr = input('Enter integer number: ')
num = int(numStr)

for i in range(4):
    numIntPart = num // 1000
    numFloorPart = num % 1000
    print('Integer part: ', numIntPart)
    print('Floor part: ', numFloorPart)
    num = numIntPart
    if not num:
        break


