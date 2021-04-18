from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        strs = ''
        def get_res(strs, left, right, n):
            if left == n and right == n:
                res.append(strs)
                return
            if left < right:
                return
            if left < n:
                get_res(strs+'(', left+1, right, n)
            if right < n:
                get_res(strs+')', left, right+1, n)
        get_res(strs, 0 , 0 ,n)
        return res