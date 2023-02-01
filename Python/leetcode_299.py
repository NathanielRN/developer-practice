from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c1 = Counter(secret)
        c2 = Counter(guess)
        total_match = 0
        for k, v in c2.items():
            if k in c1:
                total_match += min(v, c1[k])
        bulls = sum(ch1 == ch2 for ch1, ch2 in zip(secret, guess))
        cows = total_match - bulls
        return f"{int(bulls)}A{int(cows)}B"
