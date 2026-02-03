class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = {}
        
        n_squared = len(grid) * len(grid)
        a, b = 0, 0
        
        
        for row in grid:
            for i in row: 
                count[i] = count.get(i, 0) + 1
                if count[i] > 1:
                    a = i

        
        for i in range(1, n_squared + 1):
            if i not in count:
                b = i
                break
                
        return [a, b]
