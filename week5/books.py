books = set()

user_input = input('please enter name of book: ')
while user_input != 'x':
    books.add(user_input)
    user_input = input('please enter name of book: ')

print('Print books entered:')
for book in books:
    print('Book: ', book)