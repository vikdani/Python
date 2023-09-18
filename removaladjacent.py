# we have to remove the adjacent from the string and return the remianing string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1]==char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
                

    