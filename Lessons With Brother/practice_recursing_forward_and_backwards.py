from typing import List, Set, Dict

# Question: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
class Solution:
    def countOrders(self, n: int) -> int:
        #n orders
        #delivery i always after pickup i
        # Example n = 2
            # (D1, D2, P1, P2), (D2, D1, P1, P2)
        # return to modulo 10^9 + 7

        # Possible recursion question
        # Base case
        # Recursive step
        numberOfValidOrders = self.createNumberOfValidOrder(set(), list(range(n)), list(range(n)))

        # Return # of ways that a pickup/delivery can happen
        
        return numberOfValidOrders

    # [P3, P4, P5, P6, ..., P100] [D2, D3, D4]

    # orders = [P1, P2, D1, P4, D4, P3, _]

    # input_pickups = [P4, P5], input_delivers = [D4, D5]

    # current_orders = [P1, D1, P3, D3, P2, D2]

    # n = 7

    # russian dolls = [1, 2, 3, 4, 5, 6 7]

    # orders = [4, _] ->


    # (1, 2, 3)


    # current_steps = [1, 3, 2, 3, 1, 2, _]
    def createNumberOfValidOrder(self, seen_pickups: Set[int], pickups: List[int], deliveries: List[int], cache: Dict[str, int]) -> int:
        if len(deliveries) == 0:
            return 0

        key = (seen_pickups, pickups, deliveries)

        # TODO: Memoization (Bottom Up approach)
        if key in cache:
            return cache[key]

        totalValidOrders = 0

        # TODO: pickup neerds ot be in before delivery
        for index, delivery in enumerate(deliveries):
            if delivery in seen_pickups:
                newDeliveries = deliveries[:index] + deliveries[index + 1:]
                numberOfValidOrdersWhenIAddedThisDelivery = self.createNumberOfValidOrder(seen_pickups, pickups, newDeliveries)
                totalValidOrders += numberOfValidOrdersWhenIAddedThisDelivery

        for index, pickup in enumerate(pickups):
            newPickups = pickups[:index] + pickups[index + 1:]
            seen_pickups.add(pickup)
            numberOfValidOrdersWhenIAddedThisPickup = self.createNumberOfValidOrder(seen_pickups, newPickups, deliveries)
            seen_pickups.remove(pickup)
            totalValidOrders += numberOfValidOrdersWhenIAddedThisPickup

        return totalValidOrders


# "taco"

# [a, ]


# Pass Backwards

def permuteString(remainingString: str, cache: Dict[str, List[str]]) -> List[str]:
    if remainingString == "":
        return [""]

    key = remainingString
    if key in cache:
        return cache[key]
    
    allResults = []

    for index, letter in enumerate(remainingString):
        newRemainingString = remainingString[:index] + remainingString[index + 1]

        withoutLetterResults = permuteString(newRemainingString, cache) # tco, oct, toc, cot, ...
        withLetterResults = [f"{letter}{woLetterRes}" for woLetterRes in withoutLetterResults]

        allResults.extend(withLetterResults)

    cache[key] = allResults
    return allResults

def permuteString(remainingString: str, currentString: str, cache: Dict[str, List[str]]) -> List[str]:
    if remainingString == "":
        return [currentString]

    key = remainingString
    if key in cache:
        return cache[key]
    
    allResults = []

    for index, letter in enumerate(remainingString):
        newRemainingString = remainingString[:index] + remainingString[index + 1]

        withoutLetterResults = permuteString(newRemainingString, currentString, cache) # tco, oct, toc, cot, ...

        withLetterResults = [f"{letter}{woLetterRes}" for woLetterRes in withoutLetterResults]

        allResults.extend(withLetterResults)

    cache[key] = allResults
    return allResults
