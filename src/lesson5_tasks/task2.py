UPPERBOUND = 999999999999
notNumberErrorMsg = '** This in not a integer number'
tooBigNumberErrorMsg = '** Number you entered is too big'
zeroUkr = 'нуль'
singlesUkr = {'0': '', '1': 'один', '2': 'два', '3': 'три', '4': 'чотири', '5': 'п\'ять',
              '6': 'шість', '7': 'сім', '8': 'вісім', '9': 'дев\'ять', '10': 'десять', '11': 'одинадцять',
              '12': 'дванадцять', '13': 'тринадцять', '14': 'чотирнадцять', '15': 'п\'тнадцять',
              '16': 'шістнадцять', '17': 'сімнадцять', '18': 'вісімнадцять', '19': 'дев\'ятнадцять'}
tensUrk = {'2': 'двадцять', '3': 'тридцять', '4': 'сорок', '5': 'п\'тдесят', '6': 'шістдесят', '7': 'сімдесят',
           '8': 'вісімдесят', '9': 'дев\'яносто'}
hundredsUkr = {'1': 'сто', '2': 'двісті', '3': 'триста', '4': 'чотиреста', '5': 'п\'ятсот', '6': 'шістсот',
               '7': 'сімсот', '8': 'вісімсот', '9': 'дев\'ятсот'}
triads = {0: '', 1: 'тисяч(а/і)', 2: 'мільон(и/ів)', 3: 'міл\'ярд(и/ів)'}
# гарна ідея писати універсальні закінчення, щоб уникнути недорозумінь з відмінюванням

def concatStr(a, b):
    if a and b:
        _tmpstr = ' '
    else:
        _tmpstr = ''
    return str(a) + _tmpstr + str(b)


def numToString(string):
    """
    :param string:
    :return:
    """

    # також чудова ідея брати модуль від числа
    # check param is a valid integer number
    try:
        num = abs(int(string))
        # не обов"язково задавати змінну e, якщо ми її не використовуємо
    except Exception as e:
        return notNumberErrorMsg

    if num > UPPERBOUND:
        return tooBigNumberErrorMsg
    if num == 0:
        return zeroUkr

    # init vars
    resultStr = ''

    # main loop by triads (10**3)
    for i in range(len(triads)):
        # можливо ліпше робити розрахунок ділення з округленням одразу на стрічці з num = numIntPart
        # тоді ми не будемо створювати зайву змінну
        numIntPart = num // 1000
        numFloorPart = num % 1000
        # теоретично ми можемо робити приведення до строки одразу ж на 51 стрічці
        string = str(numFloorPart)
        stringLen = len(string)
        # string[-2:stringLen] -> string[-2:]
        tmpStr = singlesUkr.get(string[-2:stringLen])
        if tmpStr is None:
            # чи не ліпше використовувати  string[-1:] або string[-1]
            # адже ми беремо останній елемент з змінної string
            # Також, тоді нам не треба буде дізнаватися довжину стрічки
            tmpStr = singlesUkr.get(string[-1:stringLen], '')
            # така сама історія string[-2:-1] або ліпше string[-2]
            tmpStr = concatStr(tensUrk.get(string[-2:stringLen - 1], ''), tmpStr)
        # останнє аналогічно string[-3]
        tmpStr = concatStr(hundredsUkr.get(string[-3:stringLen - 2], ''), tmpStr)

        tmpStr = concatStr(tmpStr, triads.get(i, ''))
        resultStr = concatStr(tmpStr, resultStr)
        num = numIntPart
        if not num:
            break

    return resultStr


if __name__ == '__main__':
    numStr = input('Please enter any integer number in range 0-{0}: '.format(UPPERBOUND))
    print(numToString(numStr))
