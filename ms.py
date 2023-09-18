# mising number
from typing import List
class Solution:
    def missing_elements(self, arr: List[int]) -> int:
        sum1 = 0
        n = len(arr)+1
        while n>0:
            sum1 = sum1 + n
            n = n - 1
    
    
        sum2 = sum(arr)

        return sum1 - sum2
        
    
def main():
    n=int(input("enter num"))
    arr=[]
    s=input().split(" ")
    for i in range(0,n):
        arr.append(int(s[i]))
    
    s=Solution()
    output = s.missing_elements(arr)
    string =""
    print(output)
    
main()        