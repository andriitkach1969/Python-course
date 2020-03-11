import src.lesson6_tasks.globals as g

totalWords = 0
words = g.text.split()
outWords = []
for i in range(len(words)):
    if i % 2:
        outWords.append(words[i])
print(outWords)
print(' '.join(outWords))
