def smallest(a, b, c):
    return min(a,b,c)

def largest(a,b,c):
    return max(a,b,c)

def middle(a,b,c):
    return min(max(a,b),max(a,c),max(b,c))


number1 = (int(input('Enter a number: ')))
number2 = (int(input('Enter a second number: ')))
number3 = (int(input('Enter a third number: ')))

print(f'{smallest(number1,number2,number3)} is smallest')
print(f'{largest(number1,number2,number3)} is largest')
print(f'{middle(number1,number2,number3)} is in-between')