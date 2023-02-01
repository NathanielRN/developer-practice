from functools import cmp_to_key

a = [
    [1, True],
    [2, True],
    [3, False],
    [8, False],
    [8, True],
    [15, False],
    [15, True],
    [18, False],
    [20, True],
    [22, False],
]


def compare_events(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]

    if x[1] == y[1]:
        return 0
    elif x[1] == False and y[1] == True:
        return 1
    else:
        return -1


a.sort(key=cmp_to_key(compare_events))

print(a)
