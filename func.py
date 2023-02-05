import hashlib
def Hash(word):
    #
    # encode it to bytes using UTF-8 encoding
    hashed = hashlib.sha256(word.encode()).hexdigest()
    return hashed