class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans = []
        total = 0
        for num in str(n):
            if num == '0':
                continue
            else:
                ans.append(num)
                total+=int(num)
        
        if not ans:
            return 0

        res = int("".join(ans))
        return res*total
