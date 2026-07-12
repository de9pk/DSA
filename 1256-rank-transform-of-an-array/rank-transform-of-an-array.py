class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        n=len(arr)
        s=sorted(arr)
        ans=[]

        for x in s:
            if not ans or ans[-1] != x:
                ans.append(x)
            
        for i in range(n):
            arr[i]=bisect_left(ans,arr[i])+1
        
        return arr


