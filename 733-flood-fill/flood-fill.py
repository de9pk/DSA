class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        target = image[sr][sc]

        if target == color:
            return image

        def dfs(r, c, t, co):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if image[r][c] != t:
                return

            image[r][c] = co

            dfs(r - 1, c, t, co)
            dfs(r + 1, c, t, co)
            dfs(r, c - 1, t, co)
            dfs(r, c + 1, t, co)

        dfs(sr, sc, target, color)

        return image