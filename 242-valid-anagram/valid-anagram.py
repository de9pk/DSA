class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1  # Fixed: using s[i]
            t_count[t[i]] = t_count.get(t[i], 0) + 1  # Fixed: using t[i]

        return s_count == t_count  # Direct return