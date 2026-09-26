class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i=0
        ans=""
        knowledge = dict(knowledge)
        while i<len(s):
            if s[i]=='(':
                i+=1
                key=""
                
                while s[i]!=')':
                    key+=s[i]
                    i+=1        
                
                i+=1
                ans+=knowledge.get(key,"?")
            else:
                ans+=s[i]
                i+=1

        return ans
            



        

        
        
            
        
            


