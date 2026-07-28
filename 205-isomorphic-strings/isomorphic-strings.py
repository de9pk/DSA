class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        f1={}
        f2={}

        for char_s,char_t in zip(s,t):
            if char_s in f1 and f1[char_s] != char_t:
                return False
            
            if char_t in f2 and f2[char_t] != char_s:
                return False

            f1[char_s]=char_t
            f2[char_t]=char_s

        return True
        