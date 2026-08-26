class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans=""
        n=len(s)

        for i in range(n):
            oneCnt=0
            curr=""

            for j in range(i,n):
                curr+=s[j]
                if s[j]=='1':
                    oneCnt+=1
                if oneCnt>k:
                    break
                
                if oneCnt==k:
                    if ans=="" or len(curr)<len(ans)or(len(curr)==len(ans) and curr<ans):
                        ans=curr
                
        return ans