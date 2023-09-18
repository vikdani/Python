# we have to decode the given string, ex- '3[a]2[bc]'=aaabcbc.
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = []
        number = 0
        for char in s:
            if char.isdigit():
                number = (number*10) + int(char)
                continue
            if char=='[':
                num_stack.append(number)
                number = 0
                string_stack.append(char)
                continue
            if char!=']':
                string_stack.append(char)
                continue

            temp = []
            while string_stack[-1]!='[':
                temp.insert(0,string_stack.pop())
            string_stack.pop()

            replacement = ''.join(temp)
            count = num_stack.pop()
            replacement = replacement * count
            string_stack.append(replacement)
            result = ''.join(string_stack)
        return result            



                           

