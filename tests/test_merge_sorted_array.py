import leetcode.merge_sorted_array as msa
import pytest


def test_merge_sorted_array():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6] 
    n = 3
    result = msa.merge(nums1,m,nums2,n)

    assert nums1 == [1,2,2,3,5,6]

def test_merge_sorted_array_zero1():
    nums1 = [1]
    m = 1
    nums2 = [] 
    n = 0
    result = msa.merge(nums1,m,nums2,n)

    assert nums1 == [1]


def test_merge_sorted_array_zero2():
    nums1 = [0]
    m = 0
    nums2 = [1] 
    n = 1
    result = msa.merge(nums1,m,nums2,n)

    assert nums1 == [1]

def test_merge_sorted_array_reversed():
    nums1 = [2,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    result = msa.merge(nums1,m,nums2,n)

    assert nums1 == [1,2,2,3,5,6]

def test_merge_sorted_array_no_overlap():
    nums1 = [1,2,3,0,0,0,0]
    m = 3
    nums2 = [5,6,7,8]
    n = 4
    result = msa.merge(nums1,m,nums2,n)

    assert nums1 == [1,2,3,5,6,7,8]