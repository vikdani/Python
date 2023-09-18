from typing import List
# we have to find how much water we trap in array if it is like rainwater.
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_array = [0] * n
        right_array = [0] * n
        left_array[0] = height[0]
        right_array[n-1] = height[n-1] 

        for i in range (1,n):
            left_array[i] = max(left_array[i-1],height[i])

        for i in range (n-2,-1,-1):
            right_array[i] = max(right_array[i+1],height[i])
        result = 0
        for i in range(n):
            result += min(left_array[i],right_array[i]) - height[i] 
        return result
               

