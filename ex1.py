#Write a Python function to find the Max of three numbers

def maximal_num(a, b, c):
    if a > b or a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(maximal_num(100,11,5000))
