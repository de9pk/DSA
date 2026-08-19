class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l=max(weights)
        r=sum(weights)

        while l<=r:
            cpd=(l+r)//2 #capacity of weight per day
            cc=0 #current capacity
            dn=1 #days needed
            for w in weights:
                if cc+w>cpd:
                    dn+=1
                    cc=0
                cc+=w
                
            if dn>days:
                l=cpd+1
            else:
                r=cpd-1
            
        return l
            
                    
