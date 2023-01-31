import leetcode.remove_element as re
import pytest

def test_remove_element():
    nums = [3,3,1,1,5,7]
    val = 1
    result = re.removeElement(nums, val)

    assert result == [3,3,5,7]

def test_remove_element_simple():
    nums = [3,2,2,3]
    val = 3
    result = re.removeElement(nums, val)

    assert result == [2,2]

def test_remove_element_large_array():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = re.removeElement(nums, val)

    assert result == [0,1,3,0,4]


def test_remove_element_remove_none():
    nums = [0,1,2,2,3,0,4,2]
    val = 5
    result = re.removeElement(nums, val)

    assert result ==  [0,1,2,2,3,0,4,2]




