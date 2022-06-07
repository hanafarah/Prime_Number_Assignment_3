# pylint: disable=missing-docstring
"""
The test module for Prime Factors
It is a total of 8 test cases
"""
import pytest
from my_prime_function import prime_number_factors


def test_value_float_or_str_input():
    """
    Assert that if data type is a float or str, a ValueError is raised.
    """
    with pytest.raises(ValueError):
        raise ValueError('num value must be an int NOT float or str')


def test_num_value_1():
    """
    Assert that number value of 1, return an empty list
    """
    assert prime_number_factors(1) == []


def test_num_value_2():
    """
    Assert that number value of 2, the list [2] is returned
    """
    assert prime_number_factors(2) == [2]


def test_num_value_3():
    """
    Assert that number value of 3, the list [3] is returned
    """
    assert prime_number_factors(3) == [3]


def test_num_value_4():
    """
    Assert that number value of 4, the list [2, 2] is returned
    """
    assert prime_number_factors(4) == [2, 2]


def test_num_value_6():
    """
    Assert that number value of 6, the list [2, 3] is returned
    """
    assert prime_number_factors(6) == [2, 3]


def test_num_value_8():
    """
    Assert that number value of 8, the list [2, 2, 2] is returned
    """
    assert prime_number_factors(8) == [2, 2, 2]


def test_num_value_9():
    """
    Assert that number value of 9, the list [3, 3] is returned
    """
    assert prime_number_factors(9) == [3, 3]
