class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}

        for i in nums2:

            while stack and i > stack[-1]:
                smaller = stack.pop()
                map[smaller] = i
            
            stack.append(i)

        while stack:
            map[stack.pop()] = -1
        
        return [map[i] for i in nums1]

    