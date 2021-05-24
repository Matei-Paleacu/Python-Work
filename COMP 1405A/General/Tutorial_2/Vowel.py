def vowel_check(letter):
    if letter in ['a','e','i','o','u']:
        return f'{letter} is a vowel'
    elif letter == 'y':
        return f'{letter} is sometimes a vowel'
    else:
        return f'{letter} is not a vowel'

checked_letter = input('Enter a letter: ')

for item in checked_letter:
    print(vowel_check(item))