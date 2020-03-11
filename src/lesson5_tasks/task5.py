# initial text
text = '''
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta
sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est,
qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi
tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea
commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam
nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
'''
# гарна ідея з заданням символів кінця слова в кортеж
# set some variables
delimiters = (' ', '.', ',', '?', '!')
pos = 120
pattern = 'quis'

# на справді речень більше ніж 4, тут не враховано питальні речення
# split text into sentences and print the result
sentences = text.split('. ')
for i in sentences:
    print(i)
# count the  amount of sentences
print('Number of sentences are: ', len(sentences))

# count the amount of pattern per text
# known issues - method text.count() may count incorrectly.
print('The pattern {0} is found {1} time(s) per initial text'.format(pattern, text.count(pattern)))

# count the spaces by two different methods
print('Spaces (first method): ', text.count(' '))
count = 0
chars = [char for char in text]
for i in chars:
    if i == ' ':
        count += 1
print('Spaces (second method): ', count)

# print the number of no spaces symbols
print('number of non space symbols are: ', len(chars) - count)

# чудове рішення з обрізкою тексту
# cut the initial text to 120 symbols using "last whole word" rule
# Important suggestion - there is always space between words and after delimiters
if text[pos:pos + 1] not in delimiters:
    pos = text[0:pos + 1].rfind(' ')  # suggestion - there is always space between words and after delimiters
    if pos == -1:
        pos = 0
print('='*80)
print('Cut position: ', pos)
print(text[0:pos] + '...')


