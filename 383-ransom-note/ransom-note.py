class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rsn = {}
        mag = {}

        for i in ransomNote:
            rsn[i] = rsn.get(i,0)+1
        
        for j in magazine:
            mag[j] = mag.get(j,0)+1

        for char,count_needed in rsn.items():

            count_we_have = mag.get(char,0)

            if count_we_have<count_needed:
                return False

        return True
