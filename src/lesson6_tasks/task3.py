import src.lesson6_tasks.globals as g

ratings = {}

for word in g.text.split():
    if ratings.get(word[0].lower()) is None:
        ratings.setdefault(word[0].lower(), 1)
    else:
        ratings[word[0].lower()] = ratings.get(word[0].lower()) + 1
print(ratings)
for i in ratings:
    print(i)

maxRateKey = ''
maxRate = 0
for i in ratings:
    _tmp = ratings.get(i)
    print(_tmp)
    if maxRate < _tmp:
        maxRateKey = i
        maxRate = _tmp
        print(i)
print('The most words in text start with "{0}" char, amount {1}'.format(maxRateKey, ratings.get(maxRateKey)))
