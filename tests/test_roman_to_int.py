import leetcode.roman_to_int as rtt
import pytest

def test_roman_to_int():
    string = "III"
    result = rtt.romanToInt(string)

    assert result == 3

def test_roman_to_int_before_val():
    string = "MCMXCIV"
    result = rtt.romanToInt(string)

    assert result == 1994

def test_roman_to_int_large_val():
    string = "DCCCXXVIII"
    result = rtt.romanToInt(string)

    assert result == 828
