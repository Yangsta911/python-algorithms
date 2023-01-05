import leetcode.valid_parentheses as vp
import pytest

def test_valid_parentheses_simple_true():
    string = "()"
    result = vp.isValid(string)

    assert result == True

def test_valid_parentheses_simple_false():
    string = "(]"
    result = vp.isValid(string)

    assert result == False

def test_valid_parentheses_complex_true():
    string = "[()]{}"
    result = vp.isValid(string)

    assert result == True

def test_valid_parentheses_complex_false():
    string = "[()]{"
    result = vp.isValid(string)

    assert result == False