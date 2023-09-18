from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum = 0
        for customer in accounts:
            wealth = sum(customer)
            maxsum = max(wealth,maxsum)
        return maxsum    


            