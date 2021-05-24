'''
This is the "helper" module for Tutorial 4.

Provides the vowel_check() function to test if a character is a vowel or not.

Uses doctest commenting in the function that can be used for testing. 
Here, we write test code and the expected output (as it would appear in interactive mode)
in the docstring of the functions and the doctest module will run the code and compare 
against the expected output.
'''


def vowel_check(char):
    '''Checks if the input char is a vowel or not. 
    
    A vowel is one of a,e,i,o,u and can be upper or lower case.

    pre-condition: len(char) must be 1
    post-condition: returns True if char is a vowel, False otherwise

    >>> for c in 'aeiouAEIOU': 
    ...    vowel_check(c)
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    >>> for c in 'Pq1!':
    ...    vowel_check(c)
    False
    False
    False
    False
    '''

    vowels = 'aeiou'
    if char.lower() in vowels:
        return True 
    else:
        return False

# only run the doctest module (which tests the function)
# if this is run as a program (and NOT imported)
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)    