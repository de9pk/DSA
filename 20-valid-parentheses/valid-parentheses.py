class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for ch in s:

            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            else:

                if len(stack) == 0:
                    return False

                p = stack.pop()

                if (ch == ')' and p == '(') or \
                   (ch == ']' and p == '[') or \
                   (ch == '}' and p == '{'):

                    continue

                else:
                    return False

        return len(stack) == 0