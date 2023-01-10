import leetcode.path_sum as ps
import pytest


def test_path_sum_complex_True():
    array = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum = 22
    tree = ps.to_binary_tree(array)
    result = ps.hasPathSum(tree, targetSum, 0)

    assert result == True

def test_path_sum_simple_True():
    array = [5,2,3]
    targetSum = 7
    tree = ps.to_binary_tree(array)
    result = ps.hasPathSum(tree, targetSum, 0)

    assert result == True

def test_path_sum_simple_False():
    array = [1,3,9]
    targetSum = 12
    tree = ps.to_binary_tree(array)
    result = ps.hasPathSum(tree, targetSum, 0)

    assert result == False

def test_path_sum_complex_False():
    array = [5,4,8,11,None,13,None,15,2,None,6,None,None]
    targetSum = 95
    tree = ps.to_binary_tree(array)
    result = ps.hasPathSum(tree, targetSum, 0)

    assert result == False

def test_path_sum_complex_special():
    array = []
    targetSum = 0
    tree = ps.to_binary_tree(array)
    result = ps.hasPathSum(tree, targetSum, 0)

    assert result == False