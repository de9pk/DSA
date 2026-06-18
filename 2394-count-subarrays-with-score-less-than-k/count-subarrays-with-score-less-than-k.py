class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        l = 0
        
        for r in range(len(nums)):
            current_sum += nums[r]
            
            while current_sum * (r - l + 1) >= k:
                current_sum -= nums[l]
                l += 1
                
            count += (r - l + 1)
            
        return count