class Solution:
    def simplifyPath(self, path: str) -> str:
        part = path.split('/')
        stack = []

        for ch in part:
            if ch == "..":
                if stack:
                    stack.pop()
            elif ch == "." or ch == "":
                pass
            else:
                stack.append(ch)

        return '/'+'/'.join(stack)
        