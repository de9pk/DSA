class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        part = path.split("/")
        
        for ch in part:
            if ch == '..':
                if stack:
                    stack.pop()
            elif ch == '.' or ch == '':
                pass

            else:
                stack.append(ch)

        return '/'+'/'.join(stack)

            