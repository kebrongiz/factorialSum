def factorial_sum(num):
    if num == 1:
        return 1
    return factorial(num) + factorial_sum(num - 1)


def factorial(num):
    if (not isinstance(num, int)):
        return None
    if (num <= 1):
        return 1
    return num * factorial(num - 1)


x = int(input("Enter an integer: "))
result = factorial_sum(x)
print("The sum of the series is: {}".format(result))
