class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ans = -1
        
        for i in range(0,len(nums)):
            if nums[i] == target:
                ans = i


        return ans
                
            