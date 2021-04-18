class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        res = []
        def back(nums, tmp):
            if not nums and tmp not in res:
                res.append(tmp)
                return
            for i in range(len(nums)):
                back(nums[:i]+nums[i+1:], tmp+[nums[i]])
        back(nums, [])
        return res

