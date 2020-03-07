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
delimeters = (' ', '.', ',', '?', '!')

sentences = text.split('. ')
for i in sentences:
    print(i)
print('Number of sentences are: ', len(sentences))
print('Spaces (first method): ', text.count(' '))
count = 0
chars = [char for char in text]
for i in chars:
    if i == ' ':
        count += 1
print('Spaces (second method): ', count)
print('number of non space symbols are: ', len(chars) - count)
if text[120:121] in delimeters:
    pos = 120
else:
    pos = text[0:121].rfind(' ')  # suggestion - there is always space between words and after delimiters
    if pos == -1:
        pos = 0
print('='*80)
print('Cut position: ', pos)
print(text[0:pos] + '...')


