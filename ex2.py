#Write a Python function to calculate count of each letter in string

def count_letters(word):
    result = {}
    for i in word:
        if i not in result:
            result[i] = 1
        elif i in result:
            result[i] += 1
    return result


print(count_letters('poxos petros martiros'))
