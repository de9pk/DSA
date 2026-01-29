class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen: return True      # ← Line 1: check
            seen.add(i)                    # ← Line 2: remember
        return False
