import leetcode.maximum_depth_of_binary_tree as md
import pytest


def test_maximum_depth():
    array = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    tree = md.to_binary_tree(array)
    result = md.maxDepth(tree)

    assert result == 4


def test_maximum_depth_empty():
    array = []
    tree = md.to_binary_tree(array)
    result = md.maxDepth(tree)

    assert result == 0


def  test_maximum_depth_one():
    array = [1]
    tree = md.to_binary_tree(array)
    result = md.maxDepth(tree)

    assert result == 1


def  test_maximum_depth_simple():
    array = [3,9,20,None,None,15,7]
    tree = md.to_binary_tree(array)
    result = md.maxDepth(tree)

    assert result == 3