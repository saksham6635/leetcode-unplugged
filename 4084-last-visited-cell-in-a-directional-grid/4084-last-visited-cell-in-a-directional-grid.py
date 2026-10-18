class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        for row in grid:
            row.append(None)
        grid.append([None] * n)
        i, j = 0, 0

        while True:

            c = grid[i][j]
            grid[i][j] = None

            if c == 'L':  
                j -= 1
                if grid[i][j] is None:
                    return [i, j + 1]

            elif c == 'R': 
                j += 1
                if grid[i][j] is None:
                    return [i, j - 1]

            elif c == 'U': 
                i -= 1
                if grid[i][j] is None:
                    return [i + 1, j]

            elif c == 'D':  
                i += 1
                if grid[i][j] is None:
                    return [i - 1, j]
