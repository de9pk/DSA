class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k<=1:
            return 0

        n = len(nums)
        l = 0
        product = 1
        answer = 0

        for r in range(n):

            product *= nums[r]

            while product>=k:
                product //= nums[l]
                l+=1
            
            answer += (r-l+1)

        return answer

                
            

            


        