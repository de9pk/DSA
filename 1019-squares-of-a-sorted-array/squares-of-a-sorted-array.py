class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l = 0
        r = n-1
        arr = []

        for i in range(n):
            nums[i] *= nums[i]

        while l<=r:
            
            if nums[l] < nums[r]:
                arr.append(nums[r])
                r-=1
            else:
                arr.append(nums[l])
                l+=1

        

        return arr[::-1]
        

        

        