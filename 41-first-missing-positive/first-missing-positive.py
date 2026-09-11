class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        ans=[]
        for i in range(1,len(nums)+1):
            ans.append(i)
        nums_set = set(nums)
        for i in range(len(ans)):
            if ans[i] not in nums_set:
                return ans[i]
        
        return len(nums)+1