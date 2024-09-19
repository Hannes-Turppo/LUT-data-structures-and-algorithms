def changes(array):
    length=len(array)
    if length==1:
        return 0
    changes=0
    for i in range(1, length):
        if i==length-1:
            if array[i-1] == array[i]:
                array[i]+=array[i-1]
                changes+=1
                return changes
        if array[i-1] == array[i]:
            array[i]+=array[i+1]
            changes+=1
            continue
    return changes

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))
    print(changes([1, 2, 3, 4, 5]))
    print(changes([1, 1, 1, 1, 1]))
