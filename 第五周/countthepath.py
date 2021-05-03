from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*width for i in range(height)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for m in range(height):
            for n in range(width):
                if obstacleGrid[m][n] == 1:
                    dp[m][n] = 0
                else:
                    if m - 1 >= 0:
                        dp[m][n] += dp[m-1][n]
                    if n -1 >= 0:
                        dp[m][n] +=  dp[m][n-1]
        return dp[-1][-1]

