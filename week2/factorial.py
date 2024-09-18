print("this prongram calculater the factorial of a number.")
number = int(input("Enter a number: "))
def factorial(number):
    if number == 0:
        return 1
    else:
        for i in range(1, number):
            number *= i
        return number

print("The factorial of", number, "is", factorial(number))

# 10000! is too large to calculate 
# sys max digits (4300) exeeded
# eof
