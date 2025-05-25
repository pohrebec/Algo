import sys
import re

class HashTable:
    def __init__(self, size=200000):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0  

    def _hash(self, key):
        h = 0
        for ch in key:
            h = (h * 31 + ord(ch)) % self.size
        return h

    def add(self, key):
        h = self._hash(key)
        bucket = self.table[h]
        for k in bucket:
            if k == key:
                return 
        bucket.append(key)
        self.count += 1

    def contains(self, key):
        h = self._hash(key)
        bucket = self.table[h]
        for k in bucket:
            if k == key:
                return True
        return False

    def size(self):
        return self.count

N, M = map(int, sys.stdin.readline().split())
dict_table = HashTable()

for _ in range(N):
    w = sys.stdin.readline().strip().lower()
    dict_table.add(w)

text_lines = [sys.stdin.readline().strip() for _ in range(M)]
text = ' '.join(text_lines)
text = re.sub(r"[.,:;'\-\!\"?\(\)]", " ", text)
words_in_text = [w.lower() for w in text.split() if w]
text_table = HashTable()
for w in words_in_text:
    text_table.add(w)

unknown_found = False
for w in words_in_text:
    if not dict_table.contains(w):
        unknown_found = True
        break

if unknown_found:
    print("Some words from the text are unknown.")
else:
    missing_found = False
    for bucket in dict_table.table:
        for word in bucket:
            if not text_table.contains(word):
                missing_found = True
                break
        if missing_found:
            break

    if missing_found:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")