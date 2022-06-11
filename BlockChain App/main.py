import hashlib
h = hashlib.sha256()
h.update("a".encode())
print(h.hexdigest())
