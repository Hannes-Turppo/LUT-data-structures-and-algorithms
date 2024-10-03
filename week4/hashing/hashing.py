import hashlinear as hl

def hash(data, X):
    sum = 0
    for i in range(len(data)):
        sum += ord(data[i])
    return sum % X

