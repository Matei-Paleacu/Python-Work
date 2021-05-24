#trangleQ.py

from triangles import show

def create_triangles(x : int):
    for row_number in range(1, x+1):
        for y in range(row_number):
            show('Q')
        show('\n')

    for row_number in range(1, x+1):
        show('-')
        
    show('\n')
    
    for row_number in range(1, x+1):
        for white_space in range(x-row_number):
            show(' ')
        for y in range(row_number):
            show('Q')
        show('\n')
    
    for row_number in range(1, x+1):
        show('-')

    show('\n')
    
    for row_number in range(1, x+1):
        for y in range(x+1-row_number):
            show('Q')
        show('\n')

    for row_number in range(1, x+1):
        show('-')

    show('\n')

    for row_number in range(1, x+1):
        for white_space in range(row_number-1):
            show(' ')
        for y in range(x+1-row_number):
            show('Q')
        show('\n')

def main():
    rows = int(input('Enter a number: '))
    if rows > 1:
        create_triangles(rows)
    else:
        print('Good bye.')

#main guard
if __name__ == "__main__":
    main()