import leetcode.search_insert_position as sip
import pytest


def test_search_insert_position_in_array():
    nums = [1,3,4,5]
    target = 5
    result = sip.searchInsert(nums,target)

    assert result == 3

def test_search_insert_position_not_in_array():
    nums = [1,3,5,6]
    target = 2
    result = sip.searchInsert(nums,target)

    assert result == 1

def test_search_insert_position_first():
    nums = [2,3,5,6]
    target = 1
    result = sip.searchInsert(nums,target)

    assert result == 0