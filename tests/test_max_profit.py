import leetcode.max_profit as mp
import pytest

def test_max_profit():
    prices = [7,1,5,3,6,4]
    result = mp.maxProfit(prices)

    assert result == 5

def test_max_profit_negative():
    prices = [7,6,4,3,1]
    result = mp.maxProfit(prices)

    assert result == 0

def test_max_profit_larger_array():
    prices = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
    result = mp.maxProfit(prices)

    assert result == 43
