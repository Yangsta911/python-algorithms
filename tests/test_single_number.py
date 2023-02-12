import leetcode.single_number as sn
import pytest

def test_single_number():
    nums = [2,2,1]
    result = sn.singleNumber(nums)

    assert result == 1

def test_single_number_more_nums():
    nums = [4,1,2,1,2]
    result = sn.singleNumber(nums)

    assert result == 4


def test_single_number_one_num():
    nums = [4]
    result = sn.singleNumber(nums)

    assert result == 4