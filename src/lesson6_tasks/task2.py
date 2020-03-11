import src.lesson6_tasks.globals as g

minLen = 100

for word in g.text.split():
    # гарна ідея отримувати довжину слова 1 раз і після повторно використовувати
    _tmp = len(word)
    if minLen > _tmp:
        minLen = _tmp
print('Minimum word\'s length is {0}.'.format(minLen))


