class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        s_odd=float('inf')
        for num in nums1:
            if num % 2 == 1:
                s_odd = min(s_odd, num)

        if s_odd==float('inf'):
            return True
        
        for num in nums1:
            if num % 2 == 0 and num <= s_odd:
                return False

        return True
            