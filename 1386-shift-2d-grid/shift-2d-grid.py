class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        arr = []

        for row in grid:
            arr.extend(row)

        k%=len(arr)

        arr = arr[-k:]+arr[:-k]

        ans=[]
        index=0

        for i in range(rows):
            temp=[]
            for j in range(cols):
                temp.append(arr[index])
                index+=1
            ans.append(temp)

        return ans 