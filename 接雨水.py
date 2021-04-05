class Solution:
    def trap(self, height: [int]) -> int:
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        n = len(height)
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n-i-1] > max2:
                max2 = height[n-i-1]
            s1 += max1
            s2 += max2
        res = s1 + s2 - max1*n - sum(height)
        return res