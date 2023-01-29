import leetcode.largest_common_prefix as lcp
import pytest

def test_largest_common_prefix():
    strs = ["flower","flow","flight"]
    result = lcp.longestCommonPrefix(strs)

    assert result == "fl"


def test_largest_common_prefix_no_common():
    strs = ["dog","racecar","car"]
    result = lcp.longestCommonPrefix(strs)

    assert result == ""


def test_largest_common_prefix_all_common():
    strs = ["dog","dog","dog"]
    result = lcp.longestCommonPrefix(strs)

    assert result == "dog"