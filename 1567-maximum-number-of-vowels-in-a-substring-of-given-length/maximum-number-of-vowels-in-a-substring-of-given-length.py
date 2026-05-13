class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"a", "e", "i", "o", "u"}

        n = len(s)

        freq = 0

        for i in range(0, k):
            if s[i] in vowel:
                freq += 1

        count = freq

        for j in range(1, n - k + 1):

            if s[j - 1] in vowel:
                freq -= 1

            if s[j + k - 1] in vowel:
                freq += 1

            count = max(count, freq)

        return count
