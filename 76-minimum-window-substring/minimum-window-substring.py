class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        window = {}
        have = 0
        need = len(freq_t)

        left = 0
        res = [-1, -1]
        resLen = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in freq_t and window[ch] == freq_t[ch]:
                have += 1

            while have == need:

                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1

                if s[left] in freq_t and window[s[left]] < freq_t[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""