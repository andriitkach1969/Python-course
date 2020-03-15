ArrSymbols = ('[', ']')
ArrInc = {'[': 1, ']': -1}

ObjSymbols = ('{', '}')
ObjInc = {'{': 1, '}': -1}

ParrSymbols = ('"',)

ArrRef = 0
ObjRef = 1
ParrRef = 2

emptyChars = (' ', '\n')
depth = [0, 0, False]


def parseJson(jsonString):
    word = ''
    condensedString = ''
    for char in jsonString:
        if char not in emptyChars:
            condensedString += char
            if char in ArrSymbols:
                depth[0] += ArrInc.get(char)
            if char in ObjSymbols:
                depth[1] += ObjInc.get(char)
            if char in ParrSymbols:
                depth[ParrRef] = not depth[ParrRef]
    if sum(depth) == 0:
        print('real Json')
    return condensedString

