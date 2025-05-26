_hash_table = []
_table_size = 0
_current_books = 0
_DELETED = object()

def _hash_function(author, title, size):
    return (hash(author) + hash(title)) % size

def init():
    global _hash_table, _table_size, _current_books
    _table_size = 1000
    _hash_table = [None] * _table_size
    _current_books = 0

def _resize():
    global _hash_table, _table_size, _current_books
    old_table = _hash_table
    _table_size *= 2
    _hash_table = [None] * _table_size
    _current_books = 0
    for entry in old_table:
        if entry is not None and entry is not _DELETED:
            addBook(entry[0], entry[1])

def addBook(author, title):
    global _current_books
    if (_current_books + 1) / _table_size > 0.7:
        _resize()

    initial_hash = _hash_function(author, title, _table_size)
    for i in range(_table_size):
        index = (initial_hash + i) % _table_size
        if _hash_table[index] is None or _hash_table[index] is _DELETED:
            _hash_table[index] = (author, title)
            _current_books += 1
            return

def find(author, title):
    initial_hash = _hash_function(author, title, _table_size)
    for i in range(_table_size):
        index = (initial_hash + i) % _table_size
        if _hash_table[index] is None:
            return False
        if _hash_table[index] == (author, title):
            return True
    return False

def delete(author, title):
    initial_hash = _hash_function(author, title, _table_size)
    for i in range(_table_size):
        index = (initial_hash + i) % _table_size
        if _hash_table[index] is None:
            return
        if _hash_table[index] == (author, title):
            _hash_table[index] = _DELETED
            return

def findByAuthor(author):
    books_by_author = []
    for entry in _hash_table:
        if entry is not None and entry is not _DELETED and entry[0] == author:
            books_by_author.append(entry[1])
    books_by_author.sort()
    return books_by_author
