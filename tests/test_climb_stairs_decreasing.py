import leetcode.climbing_stairs_decreasing as csd
import pytest

def test_climbing_stairs_decreasing():
    n = 3
    result = csd.climbStairs(n)

    assert result == 3


def test_climbing_stairs_decreasing_larger_number():
    n = 10
    result = csd.climbStairs(n)

    assert result == 89


def test_climbing_stairs_decreasing_starting_cond():
    n = 1
    result = csd.climbStairs(n)

    assert result == 1
