class Solution:
    def majorityElement(self, nums):
        freq = {}
        l = len(nums)

        for n in nums:
          freq[n] = freq.get(n,0)+1

          if freq[n] > l // 2:
            return n

         
