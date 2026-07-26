class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for ch in s:
            if ch.isalnum():
                s1 = s1+ch

        s1 = s1.lower()
        rev = s1[::-1]

        return s1 == rev