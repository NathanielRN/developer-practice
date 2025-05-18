from functools import cmp_to_key


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def compare_events(x, y):
            if x[0] != y[0]:
                return x[0] - y[0]

            if x[1] == y[1]:
                return 0
            elif x[1] == False and y[1] == True:
                return 1
            else:
                return -1

        events = []

        for interval in intervals:
            start, end = interval
            events.append([start, True])
            events.append([end, False])

        events.sort(key=cmp_to_key(compare_events))

        # 1, T
        # 2, T
        # 3, T
        # 4, F
        # 7, F
        # 9, F
        # 10, T
        # 15, T
        # 15, F
        # 17, F

        # [1, 9], [10, 17]

        results = []
        current_count = 0
        current_start = None

        for event in events:
            index, is_start = event

            if current_count == 0:
                current_start = index

            if is_start:
                current_count += 1
            else:
                current_count -= 1

            if current_count == 0:
                results.append([current_start, index])
                current_start = None

        return results


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

print(a)
