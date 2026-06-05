class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        l = k

        if len(num) == k:
            return "0"

        for ch in num:
            
            while l and stack and stack[-1]>ch:
                stack.pop()
                l-=1           
            stack.append(ch)

        if l > 0:
            stack = stack[:-l]
            
        result = "".join(stack).lstrip("0")
        
        return result if result else "0"





        