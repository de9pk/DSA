class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1

        for i in count:
            if count[i] == 1:
                return i
            