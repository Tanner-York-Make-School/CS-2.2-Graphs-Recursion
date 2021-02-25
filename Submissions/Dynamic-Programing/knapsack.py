def knapsack_recursive(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
   items given."""

    if len(items) is 0 or capacity is 0:
        return 0

    first_item = items[0]
    value_with = 0

    if capacity - first_item[1] >= 0:
        value_with = first_item[2] + knapsack_recursive(items[1:], capacity-first_item[1])
    value_without = knapsack_recursive(items[1:], capacity)

    return max(value_with, value_without)


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):

            if i is 0 or j is 0:
                dp_table[i][j] = 0

            item = items[i]
            capacity = j

            value_without = dp_table[i-1][capacity]
            if item[1] < capacity:
                value_with = dp_table[i-1][capacity-item[1]] + item[2]
                dp_table[i][j] = max(value_with, value_without)
            else:
                dp_table[i][j] = value_without

    return dp_table[rows-1][cols-1]


if __name__ == '__main__':
    items = [ ('boots', 10, 60), ('tent', 20, 100), ('water', 30, 120), ('first aid', 15, 70) ]
    capacity = 50

    print(knapsack_recursive(items, capacity))
    print(knapsack_dp(items, capacity))
