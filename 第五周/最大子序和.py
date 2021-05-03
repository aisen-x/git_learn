from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sums = 0
        for num in nums:
            if sums > 0:
                sums += num
            else:
                sums = num
            ans = max(ans, sums)
        return ans