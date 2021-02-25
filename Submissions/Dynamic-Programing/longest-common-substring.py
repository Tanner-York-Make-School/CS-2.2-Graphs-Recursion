def lcs(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    if len(strA) == 0 or len(strB) == 0:
        return 0
    if strA[-1] == strB[-1]: 
        return 1 + lcs(strA[:-1], strB[:-1])
    return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))

def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(rows):
        for col in range(cols):

            if row == 0 or col == 0:
                dp_table[row][col] = 0
            elif strA[row-1] == strB[col-1]:
                prev_val = dp_table[row-1][col-1]
                dp_table[row][col] = prev_val + 1
            else:
                dp_table[row][col] = max(dp_table[row-1][col], dp_table[row][col-1])

    return dp_table[rows-1][cols-1]


if __name__ == '__main__':
    str1, str2 = 'abcde', 'adcbe'
    print(lcs(str1, str2))
    print(lcs_dp(str1, str2))
