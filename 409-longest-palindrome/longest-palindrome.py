class Solution:
    def longestPalindrome(self, s: str) -> int:

        freq = {}
        ans =0
        has_odd = False

        for i in s:
            freq[i] = freq.get(i,0)+1
        
        for count in freq.values():
            ans += (count//2)*2

            if count%2 == 1:
                has_odd=True

        if has_odd:
            ans+=1

        return ans

        

        
        