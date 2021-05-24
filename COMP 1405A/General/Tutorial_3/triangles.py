# triangle.py

def show(c):
    '''Prints c to the screen.
       Pre-condition: len(c) is 1
    '''
    if len(c) != 1:
        print("BAD input to show()!")
    print(c, end='')

def create_number_triangle(x: int):
    for row_number in range(1,x+1):
        for white_space_number in range(x-row_number):
            show(' ')
        for print_row_number in range(row_number):
            show(str(row_number))
        show('\n')
def main():
    go_again = 'y'
    while go_again == 'y':

            x = int(input('Please enter an integer between 1 and 9: '))
            if x>9 or x<1:
                print('The integer must be between 1 and 9, inclusively.')
                continue
            
            create_number_triangle(x)
            go_again = input('Would you like to draw another triangle (y/n)?' )

#main guard
if __name__ == '__main__':
    main()