class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        flip1,flip2=0,0
        for row in grid:
            for j in range(m//2):
                if row[j]!=row[m-1-j]:
                    flip1+=1
        column=list(zip(*grid))
        for row in column:
            for j in range(n//2):
                if row[j]!=row[n-j-1]:
                    flip2+=1
        return min(flip1,flip2)
        