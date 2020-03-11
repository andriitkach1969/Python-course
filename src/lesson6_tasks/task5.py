import src.lesson6_tasks.globals as g

# знову змінна яка не використовується
totalWords = 0
words = g.text.split()

# чудова ідея з розворотом в 1 стрічку коду
words[0], words[-1] = words[-1], words[0]
print(' '.join(words))
