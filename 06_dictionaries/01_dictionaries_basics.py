# A dictionary is a collection of key-value pairs.

book_01 = {'title': 'Python Crash Course',
         'author': 'Eric Matthes',
           'pages': 500}

print(f"The book {book_01['title']} has {book_01['pages']} pages or so.")


# adding new key-value pairs
book_01['press'] = 'No Starch Press'
print(book_01['press'])

# deleting a key-value pair
del book_01['press']
print(book_01)

