class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        first_val = nums.pop(0)
        min1 = nums.pop(nums.index(min(nums)))
        min2 = nums.pop(nums.index(min(nums)))
        return first_val + min1 + min2
