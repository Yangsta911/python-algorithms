import leetcode.climbing_stairs_increasing as csi
import pytest

def test_climbing_stairs_increasing():
    n = 3
    result = csi.climbStairs(n)

    assert result == 3


def test_climbing_stairs_increasing_larger_number():
    n = 10
    result = csi.climbStairs(n)

    assert result == 89


def test_climbing_stairs_increasing_starting_cond():
    n = 1
    result = csi.climbStairs(n)

    assert result == 1