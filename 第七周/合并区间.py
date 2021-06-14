from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for ele in intervals:
            if not res or res[-1][-1] < ele[0]:
                res.append(ele)
            else:
                res[-1][-1] = max(res[-1][-1], ele[-1])
        return res