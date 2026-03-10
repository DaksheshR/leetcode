def longestCommonPrefix(strs):

    first = strs[0]
    res = ""

    for j in range(len(first)):

        for i in range(len(strs)):

            if j >= len(strs[i]) or strs[i][j] != first[j]:
                return res

        res = res + first[j]

    return res
