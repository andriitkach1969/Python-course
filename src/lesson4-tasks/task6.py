namesGrid = {'mom': 'mother', 'dad': 'futher', 'sis': 'sister', 'bro': 'brother', 'dude': 'Big Lebowski'}
shortName = input('Please enter a short name: ')
try:
    fullName = namesGrid[shortName]
    print('Hello, ', fullName)
except:
    print('Sorry, we are not familiar')
