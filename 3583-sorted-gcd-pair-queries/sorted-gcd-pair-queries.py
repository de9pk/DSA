from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each number
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # pairs[d] = number of pairs having gcd exactly d
        pairs = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs[d] = c * (c - 1) // 2
            for multiple in range(2 * d, mx + 1, d):
                pairs[d] -= pairs[multiple]

        # Prefix sum of pair counts
        prefix = []
        values = []
        total = 0
        for g in range(1, mx + 1):
            if pairs[g]:
                total += pairs[g]
                prefix.append(total)
                values.append(g)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans