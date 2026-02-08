class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            # Skip duplicates
            if nums[i] == nums[i-1]:
                continue
            
            # Check if consecutive
            if nums[i] - nums[i-1] == 1:
                current_length += 1
            else:
                longest = max(longest, current_length)
                current_length = 1
        
        return max(longest, current_length)