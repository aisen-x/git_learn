class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        nums.sort()
        res=[]
        temp=[]
        def back(nums,temp):
            if not nums:
                res.append(temp)
                return
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i]==nums[i-1]:
                        continue
                    back(nums[:i]+nums[i+1:],temp+[nums[i]])
        back(nums,temp)
        return res