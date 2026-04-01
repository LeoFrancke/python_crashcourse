# A dictionary is a collection of `key` -> `value` pairs.
book_01 = {
    # 'key': 'value',
    'title': 'Python Crash Course',
    'author': 'Eric Matthes',
    'pages': 500,
    }

# accessing a value
print(f"The book {book_01['title']} has {book_01['pages']} pages or so.")


# adding new key-value pairs
book_01['press'] = 'No Starch Press'
print(book_01['press'])

# deleting a key-value pair
del book_01['pages']
print(book_01)


# avoiding Key-errors:
# use the get() method -- if the key doesn't exist, you avoid getting an error.
print(f"book name: {book_01.get('title', 'No title value assigned (clean error msg)')}")

