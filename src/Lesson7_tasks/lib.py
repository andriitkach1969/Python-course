stopSymbolsToken = (',', '}')
stopSymbolsString = stopSymbolsToken + (':',)
stopSymbolsArray = stopSymbolsString + (']',)

emptySymbols = (' ', '\n')


def condenseString(st):
    condensedString = ''
    for char in st:
        if char not in emptySymbols:
            condensedString += char
    return condensedString


def parseWord(word, st):
    length = len(word)
    _flag = False
    if st[:length] == word:
        _flag = True
        st = st[length:]
    return _flag, word, st.strip()


def parseNumber(st):
    _flag = False
    i = 0
    number = None
    for char in st:
        if char in stopSymbolsString:
            try:
                number = float(st[:i])
                _flag = True
                st = st[i:]
            except Exception as e:
                pass
            break
        i += 1
    return _flag, number, st.strip()


def parseString(st):
    _delimiter = '"'
    _resultString = None
    _flag = False
    i = 0
    for char in st:
        if char in stopSymbolsString:
            _tmpStr = st[:i]
            fPos = _tmpStr.find(_delimiter)
            lPos = _tmpStr.rfind(_delimiter)
            if lPos != fPos:
                try:
                    _resultString = str(_tmpStr[1: -1])  # get rid of quotes at both sides of string
                    _flag = True
                    st = st[i:]
                except Exception as e:
                    pass
            break
        i += 1
    return _flag, _resultString, st.strip()


def parseToken(st):
    _delimiter = ':'
    _flag = False
    _tokenName = None
    _tokenValue = None
    try:
        # parse token name
        _flag, _tokenName, st = parseString(st)
        if not _flag:
            raise Exception('** error in token name')
        # trying to parse token value
        _flag = False
        if st[0] == _delimiter:
            st = st[1:]
            _flag, _tokenValue, st = parseString(st)
            if not _flag:
                _flag, _tokenValue, st = parseNumber(st)
            if not _flag:
                _flag, _tokenValue, st = parseWord('false', st)
            if not _flag:
                _flag, _tokenValue, st = parseWord('true', st)
            if not _flag:
                _flag, _tokenValue, st = parseWord('null', st)
    except Exception as e:
        print(e)
    return _flag, {_tokenName: _tokenValue}, st.strip()


def parseObject(st):
    _delimiter = ','
    _flag = True
    res = {}
    while _flag:
        _flag, res, st = parseToken(st)
        if _flag:
            if st[0] == _delimiter:
                st = st[1:]
            yield _flag, res, st.strip()
