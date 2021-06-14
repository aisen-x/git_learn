# 动态规划(分治) 当 str1[i] = str2[j] eidt_distance(i, j) =  eidt_distance(i-1, j-1)
# 当 str1[i] != str2[j] ,eidt_distance(i, j) = min(eidt_distance(i-1, j-1)+1,
# eidt_distance(i, j-1) + 1, eidt_distance(i-1, j) + 1)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


