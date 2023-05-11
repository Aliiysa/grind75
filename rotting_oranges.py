from collections import deque

def orangesRotting(grid):
    rows, columns = len(grid), len(grid[0])
    minute, fresh = 0, 0
    q = deque()

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r,c])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dx, dy in directions:
                row, column = r + dx, c + dy
                if (row in range(rows) and column in range(columns) and grid[row][column] == 1):
                    grid[row][column] = 2
                    fresh -= 1
                    q.append([row, column])
        minute += 1
    
    return minute if fresh == 0 else -1
