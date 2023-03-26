def merge(nums1,m, nums2, n):
    temp = [0] * (m+n)
    j = 0
    k = 0
    i = 0
    while i + j < m+n:
        if i < m and j < n:
            if nums2[j] >= nums1[i]:
                temp[k] = nums1[i]
                k += 1
                i += 1
            elif nums1[i] >= nums2[j]:
                temp[k] = nums2[j]
                k += 1
                j += 1
        elif i < m:
            temp[k] = nums1[i]
            k += 1
            i += 1
        elif j < n:
            temp[k] = nums2[j]
            k +=1
            j +=1
    j = 0
    for i in temp:
        nums1[j] = i
        j += 1
    print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1

merge(nums1,m,nums2,n)