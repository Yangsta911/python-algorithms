import leetcode.remove_duplicates as rd
import pytest

def test_remove_duplicates():
    nums = [3,3,1,1,5,7]
    result = rd.removeDuplicates(nums)

    assert result == [1,3,5,7,0,0]

def test_remove_duplicates_1():
    nums = [1,1,2]
    result = rd.removeDuplicates(nums)

    assert result == [1,2,0]

def test_remove_duplicates_2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = rd.removeDuplicates(nums)

    assert result == [0,1,2,3,4,0,0,0,0,0]