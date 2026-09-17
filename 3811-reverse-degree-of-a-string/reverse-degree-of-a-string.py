class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i,ch in enumerate(s,1):
            x=ord(ch)-96
            rev=27-x
            ans+=rev*i

        return ans