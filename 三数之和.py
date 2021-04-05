# 思路：先把数组排序，取个k值，然后再用两个指针夹逼得到结果
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        nums.sort()
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            elif k > 0 and nums[k] == nums[k-1]: continue
            i, j = k+1, len(nums)-1
            while i < j:
                sum = nums[k] + nums[i] + nums[j]
                if sum < 0 :
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                elif sum > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res




