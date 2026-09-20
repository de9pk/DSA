class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        tar_len=len(part)
        t=part[-1]
        for ch in s:
            stack.append(ch)

            if ch==t and len(stack)>=tar_len:
                if "".join(stack[-tar_len:])==part:
                    del stack[-tar_len:]
            
        return "".join(stack)
            
            
        return res