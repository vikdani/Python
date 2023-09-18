from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
        
def main():
    n = int(input("enter size of array"))
    arr = []
    for i in range(n):
        arr.append(int(input("enter element of array")))
    ob = Solution()
    output = ob.runningSum(arr)
    string = " ".join(map(str,output))
    print(string)
main()    




