class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        strack = []
        heights = [0] + heights + [0]
        n = len(heights)
        res = 0
        for i in range(n):
            while strack and heights[strack[-1]] > heights[i]:
                tmp = strack.pop()
                res = max(res, (i-strack[-1]-1)*heights[tmp])
            strack.append(i)
        return  res
