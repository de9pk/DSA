class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # so this approch goes like we take the map of every number in nums2 (the greater elements map)
        stack = []
        map = {}

        for i in nums2:

            #mapping
            while stack and i > stack[-1]:
                smaller = stack.pop()
                map[smaller] = i
            
            stack.append(i)
        #reamining numbers in stack 
        while stack:
            map[stack.pop()] = -1
        
        return [map[i] for i in nums1] 

    