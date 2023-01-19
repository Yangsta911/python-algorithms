import leetcode.sqrtx as sqrt
import pytest

def test_sqrtx():
    number = 4
    result = sqrt.mySqrt(number)

    assert result == 2


def test_sqrtx_non_integer_ans():
    number = 11
    result = sqrt.mySqrt(number)

    assert result == 3

def test_sqrtx_large():
    number = 24759
    result = sqrt.mySqrt(number)

    assert result == 157

def test_sqrtx_large_integer():
    number = 3186225
    result = sqrt.mySqrt(number)

    assert result == 1785

def test_sqrtx_null():
    number = 0
    result = sqrt.mySqrt(number)

    assert result == 0

def test_sqrtxx_onel():
    number = 1
    result = sqrt.mySqrt(number)

    assert result == 1