import leetcode.twosum as ts
import pytest


def test_2_sum():
    nums = [2, 7, 11, 15]
    result = ts.twoSum(nums, 9)

    assert result == [0, 1]


def test_2_sum_1():
    nums = [3,2,4]
    result = ts.twoSum(nums, 6)

    assert result == [1, 2]

def test_2_sum_2():
    nums = [3,3]
    result = ts.twoSum(nums, 6)

    assert result == [0, 1]

def test_2_sum_3():
    nums = [0,0]
    result = ts.twoSum(nums, 6)

    assert result == []
