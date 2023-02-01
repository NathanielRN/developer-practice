import time
import sys


def solution(S):
    set1 = set(S[0])
    set2 = set()
    dict2 = {}
    total = 0
    for c in S[1:]:
        if not c in dict2:
            set2.add(c)
            dict2[c] = 1
        else:
            dict2[c] += 1
    for c in S[1:-1]:
        if len(set1) == len(set2):
            total += 1
        dict2[c] -= 1
        if dict2[c] == 0:
            set2.remove(c)
        set1.add(c)

    if len(set1) == len(set2):
        total += 1

    # sys.stderr.write(
    #     "Tip: Use sys.stderr.write() to write debug messages on the output tab.\n"
    # )
    return total


## Test cases
start_time = time.time()
assert solution("abaca") == 2, 'Wrong answer'
end_time = time.time() - start_time
print(f"Done in {end_time} seconds")
# Done in 3.409385681152344e-05 seconds
assert solution("aaaa") == 3, 'wrong answer'
