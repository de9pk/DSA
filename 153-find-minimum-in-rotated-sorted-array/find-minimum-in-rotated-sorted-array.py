class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h =n-1
        mini = float("inf")

        while l <= h:
            mid = (l+h)//2
            if nums[mid] <= nums[h]:
                mini = min(mini,nums[mid])

                h = mid - 1

            else:
                mini = min(mini,nums[l])
                l = mid+1

        return mini