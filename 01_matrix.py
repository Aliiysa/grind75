from collections import deque

def updateMatrix(mat):

    height = len(mat)
    width = len(mat[0])
    q = deque()

    for i in range(height):
        for j in range(width):
            if mat[i][j] == 0:
                q.append((i, j))
            else:
                mat[i][j] = -1
    
    while q:
        row, column = q.popleft()
        for dx, dy in ((1,0), (-1,0), (0,-1), (0, 1)):
            newRow = row + dx
            newColumn = column + dy

            if 0 <= newRow < height and 0 <= newColumn < width and mat[newRow][newColumn] == -1:
                mat[newRow][newColumn] = mat[row][column] + 1
                q.append((newRow, newColumn))
    
    return mat
