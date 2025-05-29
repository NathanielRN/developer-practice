
# 0/1

# Function to find the maximum profit
def knapsack(W, val, wt):
    
    # Initializing dp list
    dp = [0] * (W + 1)

    # Taking first i elements
    for i in range(1, len(wt) + 1):
        # Starting from back, so that we also have data of
        # previous computation of i-1 items
        for j in range(W, wt[i - 1] - 1, -1):
            not_pick = dp[j]
            pick = dp[j - wt[i - 1]] + val[i - 1]
            dp[j] = max(not_pick, pick)
    
    return dp[W]

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack(W, val, wt))

# Unbounded

# Python program to implement
# unbounded knapsack problem using space optimised

def knapSack(W, val, wt):

    # 1D matrix for tabulation.
    dp = [0] * (W + 1)

    # Calculate maximum profit for each
    # item index and knapsack weight.
    for i in range(0, len(wt)):
        for j in range(1, W + 1):
            pick = 0
            if j >= wt[i]:
                pick = val[i] + dp[j - wt[i]]

            no_pick = dp[j]

            dp[j] = max(pick, no_pick)

    return dp[W]

# 1 ... 5 ... 10 ... 15 ... 100

if __name__ == "__main__":
    val = [1, 1]
    wt = [2, 1]
    capacity = 3
    print(knapSack(capacity, val, wt))