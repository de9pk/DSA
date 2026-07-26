class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        ans = []
        for num,count in freq.items():
            if count >1:
                ans.append(num)
        
        return ans
