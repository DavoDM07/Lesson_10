#Write a Python function to calculate the factorial of a number (a non-negative
#integer). The function accepts the number as an argument.

def factorial(num):
    if num < 0:
        print(num)
        return 'error'
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result
print(factorial(int(input('Enter num '))))