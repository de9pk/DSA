class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        count=0

        def dfs(i,j):
            r=len(grid)
            c=len(grid[0])
            if i>=r or i<0 or j<0 or j>=c:
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j]=0

            return 1+dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)

        ans = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    ans=max(ans,area)

        return ans

        
        

            

