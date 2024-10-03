
def hash(S, size):
    sum = 0
    for i in range(len(S)- 1):
        sum += ord(S[i])
    return sum % 5

def bucket_chaining(keys, size):
    buckets = [None] * 5
    overflow = []
    for key in keys:
        slot = hash(key, size)
        if buckets[slot] == None:
            buckets[slot] = [key]
        elif len(buckets[slot]) == 2:
            overflow.append(key)
        else:
            buckets[slot].append(key)
    print("Overflow: ", overflow)
    return buckets


def main():
    keys = ["dog", "cat", "bird", "worm", "fish", "cow", "wolf", "fox", "seal", "fly"]
    size = len(keys)

    i=0
    buckets = bucket_chaining(keys, size)
    for key in buckets:
        print(i, key)
        i += 1


main()
