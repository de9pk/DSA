class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        f=strs[0]
        l=strs[-1]

        ans = ""
        for ch in range(min(len(f),len(l))):
            if f[ch]==l[ch]:
                ans += f[ch]
            else:
                break
        
        return ans

        