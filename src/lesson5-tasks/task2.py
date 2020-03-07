UPPERBOUND = 999999
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
thousandsUkr = {}


def concatStr(a, b):
    return str(a) + ' ' + str(b)


def numToString(string):
    """
    :param string:
    :return:
    """
    try:
        num = abs(int(string))
    except Exception as e:
        return notNumberErrorMsg

    if num > UPPERBOUND:
        return tooBigNumberErrorMsg
    if num == 0:
        return zeroUkr

    stringLen = len(string)
    resultStr = singlesUkr.get(string[-2:stringLen])
    if resultStr is None:
        resultStr = singlesUkr.get(string[-1:stringLen])
        resultStr = concatStr(tensUrk.get(string[-2:stringLen - 1]), resultStr)
    return resultStr


if __name__ == '__main__':
    numStr = input('Please enter any integer number in range 0-{0}: '.format(UPPERBOUND))
    print(numToString(numStr))

