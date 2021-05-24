def factorialWhile(n : int):
    '''Finds n! using a while loop'''
    product = n
    n -= 1
    while n > 1:
        product *= n
        n -= 1
    return product

def factorialFor(n : int):
    '''Finds n! using a for loop'''
    product = 1
    for x in range (1,n+1):
        product *= x
    return product

def numberOfVowels(s : str):
    '''Finds the number of vowels in string s'''
    vowels = ['a','e','i','o','u']
    bonk = 0
    for letter in s:
        if letter.lower() in vowels:
            bonk+=1
    return bonk
    

print('Number of vowels:',numberOfVowels('aaaaba'))
print()
print('5 Factorial', factorialWhile(5))
print()
print('5 Factorial', factorialFor(5))