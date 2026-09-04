class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        col=len(matrix[0])
        mini=[10**5+1 for _ in range(row)]
        maxi=[0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                el=matrix[i][j]
                mini[i]=min(mini[i],el)
                maxi[j]=max(maxi[j],el)

        for i in range(row):
            for j in range(col):
                el=matrix[i][j]
                if el==mini[i]==maxi[j]:
                    return [el]
        
        return []

        return -1
