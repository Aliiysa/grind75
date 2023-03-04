def floodFill(image, sr, sc, color):

    source_color = image[sr][sc]
    height = len(image)
    width = len(image[0])

    def dfs(sr, sc):

        if (0 <= sr < height) and (0 <= sc < width) and (image[sr][sc] != color) and (image[sr][sc] == source_color):
            image[sr][sc] = color

            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)

    dfs(sr, sc)

    return image

print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
