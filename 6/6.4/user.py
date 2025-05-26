_hash_table = []
_table_size = 0
_current_books = 0
_LOAD_FACTOR_THRESHOLD = 0.7

def _hash_function(author, title, size):
    return (hash(author) + hash(title)) % size

def init():
    global _hash_table, _table_size, _current_books
    _table_size = 10000
    _hash_table = [[] for _ in range(_table_size)]
    _current_books = 0

def _resize():
    global _hash_table, _table_size, _current_books
    old_table = _hash_table
    _table_size *= 2
    _hash_table = [[] for _ in range(_table_size)]
    _current_books = 0

    for chain in old_table:
        for author, title in chain:
            addBook(author, title)

def addBook(author, title):
    global _current_books
    if (_current_books + 1) / _table_size >= _LOAD_FACTOR_THRESHOLD:
        _resize()
    index = _hash_function(author, title, _table_size)

    if (author, title) not in _hash_table[index]:
        _hash_table[index].append((author, title))
        _current_books += 1

def find(author, title):
    index = _hash_function(author, title, _table_size)
    return (author, title) in _hash_table[index]

def delete(author, title):
    index = _hash_function(author, title, _table_size)
    if (author, title) in _hash_table[index]:
        _hash_table[index].remove((author, title))

def findByAuthor(author):
    books_by_author = []
    for chain in _hash_table:
        for entry_author, entry_title in chain:
            if entry_author == author:
                books_by_author.append(entry_title)
    books_by_author.sort()
    return books_by_author