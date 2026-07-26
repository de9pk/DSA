class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1

        ans = []
        while k>0:
            max_key = max(freq,key = freq.get)
            ans.append(max_key)
            del freq[max_key]
            k-=1
        
        return ans