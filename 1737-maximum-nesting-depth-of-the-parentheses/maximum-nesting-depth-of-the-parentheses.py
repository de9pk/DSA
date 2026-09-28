class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        ans=0
        for ch in s:
            if ch=="(":
                if depth>=0:
                    depth+=1
                    ans=max(ans,depth)
            
            if ch==")":
                if depth>=0:
                    depth-=1
        
        return ans
