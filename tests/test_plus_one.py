import leetcode.plus_one as po
import pytest

def test_plus_one():
    digits = [7,1,5,3,6,4]
    result = po.plusOne(digits)

    assert result == [7,1,5,3,6,5]

def test_plus_one_simple():
    digits = [1,2,3]
    result = po.plusOne(digits)

    assert result == [1,2,4]


def test_plus_one_simple_carry():
    digits = [9]
    result = po.plusOne(digits)

    assert result == [1,0]

def test_plus_one_carry():
    digits = [7,2,3,5,9]
    result = po.plusOne(digits)

    assert result == [7,2,3,6,0]


def test_plus_one_complex_carry():
    digits = [9,9,9,9,9]
    result = po.plusOne(digits)

    assert result == [1,0,0,0,0,0]