class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        pairs = sorted((num, i) for i, num in enumerate(nums))

        ans = nums[:]
        i = 0

        while i < len(pairs):
            j = i

            # Find all values belonging to the same group
            while j + 1 < len(pairs) and pairs[j + 1][0] - pairs[j][0] <= limit:
                j += 1

            # Get values and their original indices
            values = []
            indices = []

            for k in range(i, j + 1):
                values.append(pairs[k][0])
                indices.append(pairs[k][1])

            # Put smallest values at smallest indices
            indices.sort()

            for k in range(len(values)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans