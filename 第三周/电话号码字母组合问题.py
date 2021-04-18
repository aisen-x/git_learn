from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dict_ = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['x', 'w', 'y', 'z']
        }
        def helper(tmp, nextdigits):
            if len(nextdigits) == 0:
                res.append(tmp)
            else:
                for j in dict_[nextdigits[0]]:
                    helper(tmp + j, nextdigits[1:])

        res = []
        helper('', digits)
        return res
