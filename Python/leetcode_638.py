from typing import List

class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        return self.getMinCost(0, price, needs, special)

    def getMinCost(self, specialIdx, price, needs, special):
        if sum(needs) == 0:
            return 0

        if specialIdx == len(special):
            return self.getCost(price, needs)

        minCost = self.getCost(price, needs)

        for i in range(specialIdx, len(special)):
            applicable, cost, needsLeft = self.applySpecial(
                special[i], needs, 1
            )
            if applicable:
                minCost = min(
                    minCost,
                    cost + self.getMinCost(i, price, needsLeft, special),
                )

        return minCost

    def applySpecial(self, special, needs, times):
        needsLeft = needs[:]
        if times == 0:
            return True, 0, needsLeft

        for i, n in enumerate(needs):
            if special[i] * times > n:
                return False, 0, needsLeft
            needsLeft[i] -= special[i] * times

        return True, special[len(needs)] * times, needsLeft

    def getCost(self, price, needs):
        cost = 0
        for i, need in enumerate(needs):
            cost += price[i] * need
        return cost
