class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        rev_words=[]

        for ch in words:
            rev_word=ch[::-1]

            rev_words.append(rev_word)

        ans = " ".join(rev_words)
        return ans
        
            
        

            