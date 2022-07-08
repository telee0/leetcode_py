class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif stack:
                x = stack.pop()
                if c == ')' and x != '(':
                    return False
                elif c == '}' and x != '{':
                    return False
                elif c == ']' and x != '[':
                    return False
            else:
                return False
            print("c =",c , "stack =", stack)

        return len(stack) == 0


sol = Solution()
print(sol.isValid("([)]"))
print(sol.isValid("]"))
