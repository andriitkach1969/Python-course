import src.lesson6_tasks.globals as g

totalWords = 0
words = g.text.split()

words[0], words[-1] = words[-1], words[0]
print(' '.join(words))
