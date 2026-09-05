from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])

        q=deque()
        fresh=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        minute=0
        while q and fresh>0:
            size=len(q)
            for _ in range(size):
                i,j=q.popleft()
                
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    fresh-=1
                    q.append((i-1,j))
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    fresh-=1
                    q.append((i,j-1))
                if i+1<r and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    fresh-=1
                    q.append((i+1,j))
                if j+1<c and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    fresh-=1
                    q.append((i,j+1))

            minute+=1
        
        if fresh>0:
            return -1
        
        return minute
