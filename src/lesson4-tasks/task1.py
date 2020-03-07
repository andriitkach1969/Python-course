initialAmount = 500
percentage = 0.05


def calcRevenue(yearsToGo, subAmount):
    revenue = subAmount * percentage
    if yearsToGo > 1:
        revenue = revenue + calcRevenue(yearsToGo - 1, subAmount + revenue)
    return revenue


if __name__ == '__main__':
    yearsStr = input('Please enter the number of years to calculate (integer number: ')
    try:
        years = int(yearsStr)
    except Exception as e:
        print('** Error. Your entered not a valid integer number \n', e)
        exit(1)
    totalAmount = initialAmount + calcRevenue(years, initialAmount)
    print('Total amount of deposit for {0} year(s) will be:{1:8.2f}'.format(years, totalAmount))
