from collections import deque

def numIslands(grid):
    rows, columns = len(grid), len(grid[0])
    visitSet = set()
    number_islands = 0
    if not grid:
        return number_islands

    def bfs(r,c):
        q = deque()
        q.append((r,c))
        visitSet.add((r,c))

        while q:
            r, c = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dx, dy in directions:
                row, column = r + dx, c + dy
                if (row in range(rows) and column in range(columns) and (row, column) not in visitSet and grid[row][column] == "1"):
                    q.append((row, column))
                    visitSet.add((row, column))
                    


    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == "1" and (r,c) not in visitSet:
                bfs(r,c)
                number_islands += 1
    
    return number_islands
