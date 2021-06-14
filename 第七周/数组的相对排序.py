# 哈希字典加快排
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        r = [] # 存最后结果
        diff = [] # 存没在arr2出现的字符
        m = {b: 0 for b in arr2} # arr2的字典
        for num in arr1:
            if num in m:
                m[num] += 1
            else:
                diff.append(num)
        diff.sort()
        for num in arr2:
            if num in m:
                r.extend([num] * m[num])
        r.extend(diff)
        return r