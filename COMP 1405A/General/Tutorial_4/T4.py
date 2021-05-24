#T4.py
#

import helper as h
import datetime as dt

def count_vowels(s):
    '''A fuction to cout the vowels in a string'''
    vowelCount = 0
    for letter in s:
        if(h.vowel_check(letter)):
            vowelCount += 1
    return vowelCount

def dateSlice(d):
    '''formats date'''
    print(d[3:5], d[:2], d[6:], sep='/')
    print(d[6:], d[3:5], d[:2], sep='/')
    print(d[:2], d[3:5], d[6:], sep='-')

def dateSplit(d):
    '''formats date'''
    hold = d.split('/')
    date1 = (hold[1], hold[0], hold[2])
    date2 = (hold[2], hold[1], hold[0])
    date3 = (hold[0], hold[1], hold[2])
    print('/'.join(date1))
    print('/'.join(date2))
    print('-'.join(date3))

def dateFormat(d):
    '''formats date'''  
    hold = d.split('/')
    date = dt.date(int(hold[2]), int(hold[1]), int(hold[0]))

    print(date.strftime(f'%A, %B %d, %Y'))
    print(date.strftime(f'%Y/%b/%d'))
    print(date.strftime(f'%d-%m-%y (%b)'))


def number_of_hits(target, word):
    tLen = len(target)
    count = 0

    for i in range(len(word)):
        if(word[i:i+tLen] == target):
            count+=1
    return count

    
def main():
    #print(count_vowels(input("Please enter a string to count the vowels: ")))
    #dateSlice(input('Please enter a date in the format dd/mm/yyyy with the slashes: '))
    #dateSplit(input('Please enter a date in the format dd/mm/yyyy with the slashes: '))
    #dateFormat(input('Please enter a date in the format dd/mm/yyyy with the slashes: '))
    print(number_of_hits(input('What would you like to find in your word: '),input('Enter the word: ')))

if __name__ == "__main__":
    main()