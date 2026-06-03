class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(" , "}" : "{", "]" : "["}
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return not stack

s = Solution()
print(s.isValid("()"))      # True
print(s.isValid("()[]{}"))  # True
print(s.isValid("(]"))      # False
print(s.isValid("([)]"))    # False
print(s.isValid("{[]}"))    # True