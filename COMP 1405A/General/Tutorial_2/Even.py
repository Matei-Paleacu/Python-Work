def is_even(number):
    return number%2 == 0


number = None

try:
    number = int(input('Enter an integer: '))
except:
    print('bruh moment')
    exit()

if is_even(number=number):
    print(f'{number} is even.')
else:
    print(f'{number} is not even.')