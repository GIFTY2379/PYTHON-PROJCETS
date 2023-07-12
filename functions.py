# function for checking the divisibility
# notice the indentation after function declaration
# and if and else statement
def checkdivisibility(a, b):
    if a % b == 0:
        print(a, " is divisible by ", b)
    else:
        print(a, " is not divisible by ", b)


# driver program to test the above function
checkdivisibility(6, 2)
