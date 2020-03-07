symbol = input('Please input one latin symbol: ')
if symbol == '':
    print('Your input is empty, sorry')
else:
    # take just one first symbol if string entered
    symbol = symbol[0]
    if symbol.isascii() and symbol.isalpha():
        print(symbol)
        print(chr(ord(symbol)-1))
        print(chr(ord(symbol)+1))
    else:
        print('** Error. Not a latin symbol')
