# Python program to determine whether the number is
# Armstrong number or not

# Function to calculate x raised to the power y


def power(x, y):
    if y == 0:
        return 1
    p = x
    for i in range(y-1):
        p = p * x
    return p


def order(x):

    # variable to store of the number
    n = 0
    while (x != 0):
        n = n+1
        x = x//10
    return n

# Function to check whether the given number is
# Armstrong number or not


def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    d_sum = 0
    while (temp != 0):
        r = temp % 10
        d_sum += r
        sum1 = sum1 + power(r, n)
        temp = temp//10

    # If condition satisfies
    return (sum1 == x), d_sum


