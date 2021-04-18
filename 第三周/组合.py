class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        if n < k or k == 0:
            return
        res = []
        def back(i, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i, n+1):
                back(j+1, tmp+[j])
        back(1, [])
        return res