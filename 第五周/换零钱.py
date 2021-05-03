from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 转移方程 ： dp[i] = dp[i-cions] + 1
        if amount == 0:
            return 0
        res = [amount+1]*(amount+1)
        res[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    res[i] = min(res[i], res[i-c] + 1)
        if res[amount] == amount + 1: return -1
        return res[amount]