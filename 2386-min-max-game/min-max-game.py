class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        else :
            newNum = []
            maxArr = len(nums)// 2
            for i in range (0,maxArr):
                if(i%2 == 0):
                    newNum.append(min(nums[2*i], nums[2*i +1]))
                else:
                    newNum.append(max(nums[2*i] , nums[2*i+1]))

            return self.minMaxGame(newNum)

        