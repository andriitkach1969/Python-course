from src.Lesson7_tasks.lib import condenseString, parseObject

with open('Car_Model_List.json', 'r') as file:
    fullString = file.read()
    print(fullString)
    fullString = condenseString(fullString)
    print('-'*40)
    print(fullString)
    print('-'*40)

    myDict = {}
    for item in parseObject(fullString):
        print(item)
        myDict.update(item[1])
    print('-'*40)
    print(myDict)
