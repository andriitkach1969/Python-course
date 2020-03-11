import src.lesson6_tasks.globals as g

minLen = 100

for word in g.text.split():
    if minLen > len(word):
        minLen = len(word)
print('Minimum word\'s length is {0}.'.format(minLen))


