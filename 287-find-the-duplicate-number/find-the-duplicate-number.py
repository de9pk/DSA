class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = {}
        l = len(nums)

        for i in nums:
            dup[i] = dup.get(i,0) + 1
            if dup[i] > 1:
                return i
            


        
    
        