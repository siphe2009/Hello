def sum_array(array):
    x = 0
    y = 0
    while y < len(array):
        x = x + array[y]
        y = y + 1
    return x


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

def factorial(n):
    if n == 1:
        return n
    else:
        lower_fact = factorial(n-1)
        current_fact = n * lower_fact

    return  current_fact

def reverse(word):

    '''Return word in reverse'''
    result = ""
    for i in reversed(word):
         result += i
    return result
