

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float("inf")

        l = 0
        h = n-1
 

        while l < h:
            mid = (l + h) // 2

            if nums[mid] > nums[h]:
                # Minimum is in right half
                l = mid + 1
            else:
                # Minimum is in left half (including mid)
                h = mid

        return nums[l]