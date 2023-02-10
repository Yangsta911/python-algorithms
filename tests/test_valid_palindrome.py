import leetcode.valid_palindrome as vp
import pytest

def test_valid_palindrome():
    s = "A man, a plan, a canal: Panama"
    result = vp.isPalindrome(s)

    assert result == True


def test_valid_palindrome_simple_false():
    s = 'race a car'
    result = vp.isPalindrome(s)

    assert result == False


def test_valid_palindrome_simple_empty():
    s = ''
    result = vp.isPalindrome(s)

    assert result == True


def test_valid_palindrome_only_non_character_empty():
    s = ':<:">{}(?)/@!#$%'
    result = vp.isPalindrome(s)

    assert result == True

def test_valid_palindrome_false_non_characters():
    s = 'asdfgm#$wgkfg@'
    result = vp.isPalindrome(s)

    assert result == False


def test_valid_palindrome_false_non_characters_with_spaces():
    s = 'as dfgm #$wgk fg@'
    result = vp.isPalindrome(s)

    assert result == False

