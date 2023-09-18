# we have to arrange the paranthesis in correct order
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if stack and stack[-1]==mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack)==0
                
def main():
    n=input()
    s=Solution()
    output = s.isValid(n)
    if(output):
        print("true")
    else:
        print("false")
    
main()