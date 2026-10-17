class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Correctly compute digit sums
        def get_digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        
        # 2. Pair each number as (digit_sum, value) and sort.
        # Python naturally breaks ties using the second tuple element (smaller value first).
        sorted_arr = sorted((get_digit_sum(x), x) for x in nums)
        
        # 3. Create a map that tells us where each number *needs* to go
        target_index = {val: i for i, (d_sum, val) in enumerate(sorted_arr)}
        
        # 4. Count the cycles
        visited = [False] * n
        min_swaps = 0
        
        for i in range(n):
            # If the element is already in its correct position or already visited, skip it
            if visited[i] or target_index[nums[i]] == i:
                continue
                
            # Trace the loop (cycle)
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = target_index[nums[j]]  # Jump to where the number at j is supposed to go
                cycle_size += 1
                
            # A cycle of length k takes k - 1 swaps to fix
            if cycle_size > 0:
                min_swaps += (cycle_size - 1)
                
        return min_swaps
