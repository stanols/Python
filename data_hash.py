import hashlib;

#returns hash value for input string
def getHash(text):
    return hashlib.sha256(text.encode()).hexdigest();
