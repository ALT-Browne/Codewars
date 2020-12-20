def lcs(x, y):
    """
    Finds longest common subsequence by first removing unnecessary characters and then iterating over all common subsequences starting with a given character in the shorter resulting list.
    """
    new_x = "".join([char for char in x if char in y])
    new_y = "".join([char for char in y if char in x]) # Only need common characters
    if len(new_x) == 0 or len(new_y) == 0:
        return ""
    max_subsequence = new_x[0]
    if len(new_x) <= len(new_y):
        list_1 = new_x
        list_2 = new_y
    else:
        list_1 = new_y
        list_2 = new_x
    for i in range(len(list_1)):
        subsequence_list_1_index_list = [i]
        subsequence_list_2_index_list = [list_2.index(list_1[i])]
        start = list_2.index(list_1[i])
        for k in range(i + 1, len(list_1)):
            for j in range(start + 1, len(list_2)):
                if list_2[j] == list_1[k]:
                    subsequence_list_1_index_list.append(k)
                    subsequence_list_2_index_list.append(j)
                    start = j
                    break
        if len(subsequence_list_1_index_list) > len(max_subsequence):
            max_subsequence = "".join([list_1[l] for l in subsequence_list_1_index_list])
    return max_subsequence


def lcs_2(x, y):
    """
    Recursive method which uses the fact that any common subsequence for two strings can be extended by adding the same letter to the end of each string.
    """
    if len(x) == 0 or len(y) == 0:
        return ""
    if x[-1] == y[-1]:
        return lcs_2(x[:-1], y[:-1]) + x[-1]
    else:
        reduce_y = lcs_2(x, y[:-1])
        reduce_x = lcs_2(x[:-1], y)
        if len(reduce_y) > len(reduce_x):
            return reduce_y
        else:
            return reduce_x
