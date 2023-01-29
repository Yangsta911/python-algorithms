def longestCommonPrefix(strs):
    comparison_array = strs[0]
    prefix_counter = 0
    for i in range(1,len(strs)):
        temp_arr = strs[i]
        counter = 0
        temp_prefix = 0
        test = len(temp_arr)
        while counter < len(comparison_array) and counter < len(temp_arr):
            if temp_arr[counter] == comparison_array[counter]:
                temp_prefix += 1
            counter += 1
        if temp_prefix != prefix_counter:
            prefix_counter = temp_prefix

    prefix = ""
    for j in range (0, prefix_counter):
        prefix = prefix + comparison_array[j]

    return prefix


strs = ["flower","flow","flight"]
longestCommonPrefix(strs)