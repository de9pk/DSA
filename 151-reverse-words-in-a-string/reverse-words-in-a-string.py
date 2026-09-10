class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        word_list=s.split()

        for word in range(len(word_list)-1,-1,-1):
            res.append(word_list[word])
        
        return " ".join(res)

        