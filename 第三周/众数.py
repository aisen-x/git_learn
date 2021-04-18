#摩尔投票解决众数问题
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = b = None
        na = nb = 0
        for num in nums:
            if num == a:
                na+=1
            elif num == b:
                nb+=1
            elif not na:
                a, na = num, 1
            elif not nb:
                b, nb = num, 1
            else:
                na -= 1
                nb -= 1
        na = nb = 0
        for num in nums:
            if a == num:
                na += 1
            elif b == num:
                nb += 1
        return [i for i, c in zip((a, b), (na, nb)) if c > len(nums)//3]



