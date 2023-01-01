def main():
    nums = [3,7,5,2,1,1,3]
    removeDuplicates(nums)

def insertion_sort(A, i = None):
    if i is None: i = len(A) - 1
    if i > 0:
        insertion_sort(A, i - 1)
        insert_last(A, i)

def insert_last(A, i):
    if i > 0 and A[i] < A[i - 1]:
        A[i], A[i - 1] = A[i - 1], A[i]
        insert_last(A, i - 1)

def removeDuplicates(nums):
    insertion_sort(nums)
    counter = 0
    array = [0] * len(nums)
    for j in nums:
        if counter == 0:
            array[counter] = j
            counter += 1
        else:
            if array[counter - 1] != j:
                array[counter] = j
                counter += 1
    return array


main()