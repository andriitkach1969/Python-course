lexeme = ('парне', 'непарне')

bottomBoundStr = input('Введить початкове ціле число: ')
topBoundStr = input('Введіть кінцеве ціле число: ')

try:
    topBound = int(topBoundStr)
    bottomBound = int(bottomBoundStr)
    for i in range(bottomBound, topBound):
        print(i, ' ', lexeme[i % 2])
except Exception as e:
    print('** Error. Неправильно введені числа \n')
    print(e)