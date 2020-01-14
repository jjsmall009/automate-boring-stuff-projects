"""Calculates the collatz sequence for a given integer.

The Collatz Conjecture (or 3n + 1 problem) is a cool math thing.  This module will
showcase the sequence by printing out the steps as it computes down to 1. Yeah.

JJ Small - 1/4/20
"""

def collatz(num):
    """Calculates the collatz sequence for a given integer.

    Parameters:
    num (int): The starting number for the sequence

    Returns:
    int: If num is even it will return n // 2, otherwise it will return 3 * num + 1
    """
    try:
        while num != 1:
            if num < 0:
                print('Error: Value must be an integer greater than 0.')
                return

            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            
            print('Next step in sequence: %s' % num)
    except TypeError:
        print('Error: Value must be an integer 1.')

def user_loop():
    """Prompt the user for their starting integer"""

    try:
        num = input('Enter the starting value for your collatz sequence: ')
        collatz(int(num))
    except TypeError:
        print('Error: Value must be an integer 2.')

user_loop()


