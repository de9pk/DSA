

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float("inf")

        for i in range(n):
            mini = min(mini, nums[i])

        return mini