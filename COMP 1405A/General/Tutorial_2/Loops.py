def counting_up(start,stop):
    to_print = ''
    while start < stop:
        to_print = to_print+f'{start}, '
        start+=1
    to_print = to_print[0:len(to_print)-2]
    return to_print


def counting_down(start,stop):
    to_print = ''
    while start > stop:
        to_print = to_print+f'{start}, '
        start-=1
    to_print = to_print[0:len(to_print)-2]
    return to_print


# print(counting_up(1,10))
# print(counting_down(10,7))

number1 = int(input('Enter a starting number: '))
number2 = int(input('Enter a stopping number: '))

if number1 < number2:
    print(counting_up(number1,number2))
else:
    print(counting_down(number1,number2))