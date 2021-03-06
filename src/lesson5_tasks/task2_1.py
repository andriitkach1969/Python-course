#import src.lesson5_tasks.task2_1_globals as g
import task2_1_globals as g

# чудова ідея з використанням функцій та винесенням чисел в глобальні змінні
# щодо коду див файл task2.py
# коментарі актуальні й для цього файлу

def concatStr(a, b):
    """
    Function concatenates two string and insert space between if they are not empty
    :arg a: first string to concatenate
    :type a: basestring
    :arg b: second string to concatenate
    :type b: basestring
    :return: concatenated string
    :rtype: basestring
    """
    if a and b:
        _tmpstr = ' '
    else:
        _tmpstr = ''
    return str(a) + _tmpstr + str(b)


def numToString(string):
    """
    Function converts number represented as string into text in decimal number system
    :param string: number represented as string
    :type string: basestring
    :return: text in human format
    :rtype: basestring
    """
    # check param is a valid integer number
    try:
        num = abs(int(string))
    except Exception as e:
        return g.notNumberErrorMsg

    if num > g.UPPERBOUND:
        return g.tooBigNumberErrorMsg
    if num == 0:
        return g.zeroUkr

    resultStr = ''

    # main loop by triads (10**3)
    for i in range(len(g.triads)):
        numIntPart = num // 1000
        numFloorPart = num % 1000

        string = str(numFloorPart)
        stringLen = len(string)

        # proceed the two lowest digits for some cases
        _tmp = string[-2:stringLen]
        tmpStr = g.singlesUkr.get(_tmp)
        if tmpStr is None:
            # proceed the lowest digit from current triad
            _tmp = string[-1:stringLen]
            tmpStr = g.singlesUkr.get(_tmp, '')
            # proceed second digit from current triad. if it absents - use empty string
            tmpStr = concatStr(g.tensUrk.get(string[-2:stringLen - 1], ''), tmpStr)
        # save position for triad's cases
        casePosition = int(_tmp)
        # proceed the highest digit from current triad. if it absents - use empty string
        tmpStr = concatStr(g.hundredsUkr.get(string[-3:stringLen - 2], ''), tmpStr)

        # add the triad name
        tmpStr = concatStr(tmpStr, g.triads.get(i).get((lambda x: x if x in (1, 2, 3, 4) else 0)(casePosition)))
        # concat with previous step result
        resultStr = concatStr(tmpStr, resultStr)

        num = numIntPart
        if not num:
            break

    return resultStr


if __name__ == '__main__':
    numStr = input('Please enter any integer number in range 0-{0}: '.format(g.UPPERBOUND))
    print(numToString(numStr))
