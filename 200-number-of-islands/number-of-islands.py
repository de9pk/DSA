class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        count=0

        def dfs(i,j,grid):
            r=len(grid)
            c=len(grid[0])
            if i>=r or i<0 or j<0 or j>=c:
                return
            if grid[i][j]!='1':
                return 
            
            grid[i][j]='x'

            dfs(i-1,j,grid)
            dfs(i,j-1,grid)
            dfs(i+1,j,grid)
            dfs(i,j+1,grid)

        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j,grid)
        
        return count