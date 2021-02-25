def edit_distance(str1, str2, m, n):
    """Compute the Edit Distance between 2 strings."""
    if m == 0:
        return n
    
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)

    insert = edit_distance(str1, str2, m, n-1)
    remove = edit_distance(str1, str2, m-1, n)
    replace = edit_distance(str1, str2, m-1, n-1)
    return min(insert, remove, replace) + 1


def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(rows):
        for col in range(cols):

            if row == 0:
                dp_table[row][col] = col
            elif col == 0:
                dp_table[row][col] = row
            elif str1[row-1] == str2[col-1]:
                dp_table[row][col] = dp_table[row-1][col-1]
            else:
                insert = dp_table[row][col-1]
                remove = dp_table[row-1][col]
                replace = dp_table[row-1][col-1]
                dp_table[row][col] = min(insert, remove, replace) + 1

    return dp_table[rows-1][cols-1]

if __name__ == '__main__':
    str1, str2 = 'sunday', 'saturday'
    print(edit_distance(str1, str2, len(str1), len(str2)), 3)
    print(edit_distance_dp(str1, str2), 3)