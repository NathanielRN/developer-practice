from typing import List

# Merge Sort is a Divide & Conquer

def mergesort(unsorted_list: List[int]) -> List[int]:
    return _mergesort(unsorted_list, 0, len(unsorted_list))

def _mergesort(unsorted_list: List[int], start: int, end: int) -> List[int]:
    if start == end:
        return [unsorted_list[start]]

    mid = len(unsorted_list) // 2
    # 2 33 64 97
    # 1 45 78 100
    left = _mergesort(unsorted_list, 0, mid)
    right = _mergesort(unsorted_list, mid + 1, end)

    # How Zip works:

    # Start:
    # [
        # [1, 2, 3, 4, 5]
        # [A, B, C, D, E, F, G]
    # ]

    # 1st zip:
    # [
        # [1, A],
        # [2, B],
        # [3, C],
        # [4, D]
        # [5, E]
    # ]

    # 2nd zip:
    # [
        # [1, 2, 3, 4, 5]
        # [A, B, C, D, E, F, G]
    # ]

    # but you can't do zip, because merge sort is about moving indices ahead of
    # each other.
    # for l, r in zip(left, right):

    merged = []

    l = 0
    r = 0

    while l < len(left) and r < len(right):
        l_value = left[l]
        r_value = right[r]

        if l_value > r_value:
            merged.append(r_value)
            r += 1
        else:
            merged.append(l_value)
            l += 1

    if l == len(left):
        merged.extend(right[r:])
    else:
        merged.extend(left[l:])

    return merged
