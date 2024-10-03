def hash(key, size):
    return key % size

def linear_probing(keys):
    size = 10
    table = [10, None, None, 53, None, 35, 66, None, None, 19]
    for key in keys:
        slot = hash(key, size)
        if table[slot] == None:
            table[slot] = key
        else:
            i = 1
            while table[(slot + i) % size] != None:
                i += 1
            table[(slot + i) % size] = key
    return table

def main():
    keys = [91, 103, 79, 247, 9]
    table = linear_probing(keys)
    for i in range(len(table)):
        print(i, table[i])

main()
