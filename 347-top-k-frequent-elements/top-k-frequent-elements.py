class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stack = []
        ans = []
        max_pair = 0
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1

        for j in freq:
            stack.append((freq[j], j))  # (frequency, actual number)

        while k:
            max_pair = max(stack)        # max by frequency (first element of tuple)
            ans.append(max_pair[1])      # append the actual number
            stack.remove(max_pair)
            k -= 1

        return ans


