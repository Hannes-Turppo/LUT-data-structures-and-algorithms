def recursion(x):
    if x == 0:
        return 1
    else:
        return recursion(x-1) + recursion(x-1)

number = int(input("Give a number for recursion: "))
print(recursion(number))
