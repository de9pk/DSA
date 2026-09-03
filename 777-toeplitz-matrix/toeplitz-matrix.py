class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        row=len(mat)
        col=len(mat[0])

        for i in range(1,row):
            for j in range(1,col):
                if mat[i][j]!=mat[i-1][j-1]:
                    return False
        
        return True