# Two array are given , pushed and popped, we have to check whether the push and pop operations are in correct sequence or not, return true if the sequence is correct

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        for nums in pushed:
            stack.append(nums)
            while stack and stack[-1]==popped[pop_index]:
                stack.pop()
                pop_index = pop_index + 1
        return len(stack)==0
            
        