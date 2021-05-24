def is_divisible(x,y):
    return x%y == 0


number1 = None
number2 = None

try:
    number1 = int(input('Enter an integer: '))
    number2 = int(input('Enter a second integer: '))
except:
    print('bruh moment')
    exit()

if is_divisible(number1,number2):
    print(f'{number1} is evenly divisble by {number2}.')
else:
    print(f'{number1} is not evenly divisble by {number2}.')