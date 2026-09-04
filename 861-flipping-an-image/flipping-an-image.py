class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for mat in image:
            mat.reverse()
        
        for mat in image:
            for i in range(len(mat)):
                if mat[i]==1:
                    mat[i]=0
                else:
                    mat[i]=1
            
        return image