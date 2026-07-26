class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        if len(nums)==0:
            return 0
        longest =1
        current =1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            elif nums[i+1]-nums[i]==1:
                current+=1
            else:
                longest = max(longest,current)
                current =1
        
        return max(longest,current)
