import calendar
import re

# чудова ідея з винесенням марсеру в окрему функцію, а також коментарем
# також добре, що ми отримуємо userfriendly повідомлення
def parseDate(dateStr):
    """
    Function parse input string in strict format DD-MM-YYYY into separate integer day, month and year
    :param dateStr: string in format DD-MM-YYYY
    :type dateStr: string
    :return: set consist of 3 elements (day, month, year)
    :rtype: set
    :
    """
    errorFormatMsg = '** Error. Wrong date format. Expected "DD-MM-YYYY"'
    errorDayMsg = '** Error. Wrong day. Expected in range 1-31'
    errorMonthMsg = '** Error. Wrong month. Expected in range 1-12'
    errorYearMsg = '** Error. Wrong year. Expected in range 1970-9999'

    # також гарна ідея з regex
    datePattern = r'\d{2}[-*/]\d{2}[-*/]\d{4}'

    # check if param string is matching to required pattern
    try:
        if not re.fullmatch(datePattern, dateStr):
            raise Exception
        _day = int(dateStr[0:2])
        _month = int(dateStr[3:5])
        _year = int(dateStr[6:10])
    except:
        print(errorFormatMsg)
        exit(1)

    # check the date is valid
    try:
        if not 1 <= _day <= 31:
            raise Exception(errorDayMsg)
        if not 1 <= _month <= 12:
            raise Exception(errorMonthMsg)
        if not 1970 <= _year <= 9999:
            raise Exception(errorYearMsg)
    except Exception as e:
        print(e)
        exit(1)
    return _day, _month, _year


if __name__ == '__main__':
    # можна розділити логіку порожньою стрічкою, це дозволить легше сприймати код
    # але в контексті цього файлу це не обов"язково
    searchDateStr = input('Please enter a date in format dd-mm-yyyy: ')
    (day, month, year) = parseDate(searchDateStr)

    (tmp, daysTotal) = calendar.monthrange(year, month)
    print('in {0} {1} are {2} days totally.'.format(calendar.month_name[month], year, daysTotal))
    
    weekDay = calendar.weekday(year, month, day)
    if weekDay in (calendar.SATURDAY, calendar.SUNDAY):
        print('Entered day is weekend')
