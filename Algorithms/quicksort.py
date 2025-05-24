from typing import List

# def quicksort(unsorted_list: List[int]) -> None:
#     _quicksort(unsorted_list, 0, len(unsorted_list))

# def _quicksort(unsorted_list: List[int], start: int, end: int) -> None:
#     if end - start <= 1:
#         return

#     pivot = (end + start) // 2
#     pivot_value = unsorted_list[pivot]
#     unsorted_list[pivot] = unsorted_list[end - 1]

#     low = start
#     high = end - 2

#     # low <= high gives low a chance to move to the last element and say it
#     # doesn't want to swap anything for the pivot and so avoids swapping out
#     # the pivot by accident.
#     while low <= high:
#         # low != end - 1 also allows low to say "everything in the list is
#         # already smaller than the pivot" and not want to swap anything.
#         while unsorted_list[low] < pivot_value and low != end - 1:
#             low += 1

#         # high != start - 1 is important because high needs to say "everything
#         # in the list was already bigger than the pivot" and it needs to break
#         # out of the `low <= high` while loop. Anyways `low` is what will
#         # decide the swap so we don't care of high goes out of bounds
#         while unsorted_list[high] > pivot_value and high != start - 1:
#             high -= 1

#         if low < high:
#             temp = unsorted_list[high]
#             unsorted_list[high] = unsorted_list[low]
#             unsorted_list[low] = temp

#     unsorted_list[end - 1] = unsorted_list[low]
#     unsorted_list[low] = pivot_value

#     _quicksort(unsorted_list, start, low)
#     _quicksort(unsorted_list, low + 1, end)

# ChatGPT's more simple answer
from typing import List

def quicksort(arr: List[int]) -> None:
    def _quicksort(start: int, end: int) -> None:
        if end - start <= 1:
            return

        pivot = arr[end - 1]
        low = start

        for j in range(start, end - 1):
            if arr[j] <= pivot:
                arr[low], arr[j] = arr[j], arr[low]
                low += 1

        arr[low], arr[end - 1] = pivot, arr[low]
        _quicksort(start, low)
        _quicksort(low + 1, end)

    _quicksort(0, len(arr))

# Testcase 1
a = [13, 77, 49, 35, 61, 48, 73, 23, 95, 3, 89, 37, 57, 99, 17, 32, 94, 28, 15, 55, 7, 51, 88, 97, 62]
expected = sorted(a)
quicksort(a)

assert expected == a

# Testcase 2
a = [5, 4, 3, 2, 1]
expected = sorted(a)
quicksort(a)
assert expected == a

# Testcase 3
a = [5, 4, 3, 3, 3, 3, 3, 2, 1]
expected = sorted(a)
quicksort(a)
assert a == expected
