class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        arr = []
        n = len(nums)
        for i in range(len(nums)):
            if n == 0:
                return -1

            x = nums[i]*nums[i]
            arr.append(x)

        arr.sort()

        return arr

        