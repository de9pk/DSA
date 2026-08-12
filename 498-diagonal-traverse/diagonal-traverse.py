class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r=len(mat)
        c=len(mat[0])

        res=[]
        curr_r=curr_c=0

        for _ in range(r*c):
            res.append(mat[curr_r][curr_c])

            if (curr_r+curr_c)%2==0:
                if curr_c==c-1:
                    curr_r+=1
                elif curr_r==0:
                    curr_c+=1
                else:
                    curr_r-=1
                    curr_c+=1
            else:
                if curr_r==r-1:
                    curr_c+=1
                elif curr_c==0:
                    curr_r+=1
                else:
                    curr_c-=1
                    curr_r+=1

        return res
