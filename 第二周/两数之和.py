class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        dict_ = {}
        for i in range(len(nums)):
            if nums[i] in dict_:
                return [dict_[nums[i]], i]
            else:
                dict_[target-nums[i]] = i



