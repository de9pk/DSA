class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for i in range(len(s)-1):            
            if i+1>len(s):
                return
            x=abs(ord(s[i])-ord(s[i+1]))
            ans+=x

        
        return ans