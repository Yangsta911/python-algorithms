import leetcode.sqrtx_loop as sl
import pytest

def test_sqrtx_loop():
    number = 4
    result = sl.mySqrt(number)

    assert result == 2


def test_sqrtx_loop_non_integer_ans():
    number = 11
    result = sl.mySqrt(number)

    assert result == 3

def test_sqrtx_loop_large():
    number = 24759
    result = sl.mySqrt(number)

    assert result == 157

def test_sqrtx_loop_large_integer():
    number = 3186225
    result = sl.mySqrt(number)

    assert result == 1785
