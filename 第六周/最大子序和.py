from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]):
        ans = nums[0]
        sum = 0
        for num in nums:
            if num > 0:
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
        return ans