import src.lesson6_tasks.globals as g

totalWords = 0
findWords = 0

char = input('Please enter one symbol to search: ')
for word in g.text.split():
    totalWords += 1
    if word[0] == char:
        findWords += 1
print('There are {0} words in text and {1} of its start(s) with symbol {2}.'.format(totalWords, findWords, char))
print('That is {0} percentage'.format(findWords / totalWords * 100))
