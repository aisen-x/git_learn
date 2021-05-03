from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 转移方程： dp[i] = max(dp[i-2]+ nums[i], dp[i-1])
        last = 0
        now = 0
        for i in nums:
            last, now = now, max(last+i, now)
        return now