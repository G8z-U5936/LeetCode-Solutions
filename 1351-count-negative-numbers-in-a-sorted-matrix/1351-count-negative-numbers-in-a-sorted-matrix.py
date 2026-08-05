class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                num = grid[i][j]
                if num < 0:
                    count += 1
                    print(count)
        return count