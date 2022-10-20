class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validParen = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in validParen:
                if(stack and stack[-1] == validParen[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
