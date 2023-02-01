import leetcode.length_of_last_word as lotw
import pytest

def test_length_of_last_word():
    s = "Hello World"
    result = lotw.lengthOfLastWord(s)

    assert result == 5

def test_length_of_last_word_spaces_at_end():
    s = "   fly me   to   the moon  "
    result = lotw.lengthOfLastWord(s)

    assert result == 4


def test_length_of_last_word_one_word():
    s = "test"
    result = lotw.lengthOfLastWord(s)

    assert result == 4


def test_length_of_last_word_one_word_with_space_after():
    s = "test         "
    result = lotw.lengthOfLastWord(s)

    assert result == 4


def test_length_of_last_word_long_word():
    s = "test  hello world  kijtrkajsgljaslkgjsdghadfhgsg"
    result = lotw.lengthOfLastWord(s)

    assert result == 29
