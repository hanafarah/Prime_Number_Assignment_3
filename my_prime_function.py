"""
Created prime.py -- Write the application code here

This function will take a number and will ouput as a list of prime numbers.

"""


def prime_number_factors(num):
    """
    This function will take a number and will ouput as a list of prime numbers.
    """
    list_of_factors = []  # should be an empty list. Output will generate as a list
    dividing_factor = 2   # divisble factor to determine prime numbers

    if isinstance(num, int):  # to determine if num is an int in order to pass through
        while num > 1:

            if num % dividing_factor == 0:
                # num is divisible then add to the list
                list_of_factors.append(dividing_factor)
                num = num/dividing_factor
                dividing_factor -= 1
            dividing_factor += 1

    return list_of_factors
