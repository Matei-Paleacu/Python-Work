def is_divisible(x,y):
    return x%y == 0


number = None

try:
    number = int(input('Enter an integer: '))
except:
    print('bruh moment')
    exit()

for item in range(2,7):
    if is_divisible(number, item):
        print(f'{number} is divisble by {item}')
    else:
        print(f'{number} is not divisble by {item}')