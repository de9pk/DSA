class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:  # FIXED: proper indent
                return True
            seen.add(num)    # FIXED: proper indent
            if i >= k:       # FIXED: proper indent
                seen.remove(nums[i - k])
        return False         # ADDED: missing return
