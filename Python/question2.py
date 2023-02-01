import sys


def solution(A):
    # #1509 on Leetcode
    if len(A) <= 3:
        return 0

    A.sort()
    ans = A[-1] - A[0]

    windows_size = len(A) - 1 - 3
    for i in range(4):
        diff = A[i + windows_size] - A[i]
        if diff < ans:
            ans = diff

    return ans

# 0 4 1

# -1 3 3 4


ans = solution([-9, 8, -1])
assert ans == 0, f"Failed: {ans}"
ans = solution([14, 10, 5, 1, 0])
assert ans == 1, f"Failed: {ans}"
ans = solution([11, 0, -6, -1, -3, 5])
assert ans == 3, f"Failed: {ans}"
ans = solution([10, 10, -6, 2, -3, 10])
assert ans == 0, f"Failed: {ans}"
ans = solution([8, -1, 4, 3, 5, -1])
assert ans == 2, f"Failed: {ans}"

ans = solution([-49, -48, -25, -20, -15, -10, -5, 0, 5, 10, 11, 12])
assert ans == 32, f"Failed: {ans}"

ans = solution([-50, -49, -48, -47, -25, -20, -15, -10, -5, 0, 5, 10, 11, 12])
assert ans == 55, f"Failed: {ans}"

ans = solution([-50, -49, -48, -25, -20, -15, -10, -5, 0, 5, 10, 11, 12])
assert ans == 37, f"Failed: {ans}"