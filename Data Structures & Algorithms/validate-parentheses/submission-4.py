class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(':')','{':'}' ,'[':']'}
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')' or char == ']' or char == '}':
                if not stack:
                    return False
                if dict[stack.pop()] != char:
                    return False
        if stack:
            return False
        return True