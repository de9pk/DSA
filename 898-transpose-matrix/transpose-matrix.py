class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])

        ans=[]
        for j in range(c):
            row=[]
            for i in range(r):
                row.append(matrix[i][j])
            ans.append(row)

        return ans