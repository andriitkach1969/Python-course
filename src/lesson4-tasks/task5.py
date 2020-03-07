numberStr = input('Please input any integer number: ')
if numberStr.isdigit():
    total = 0
    numberLen = len(numberStr)
    for i in range(0, numberLen):
        total += int(numberStr[i])
    print('The entered number consists of {0} digits and its sum is {1}'.format(numberLen, total))
else:
    print('** Error. Your entered not a valid integer number \n', e)
