from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        def mergesort(nums, start, end, tmp):
            if start >= end:
                return
            mid = (start + end) >> 1
            mergesort(nums, start, mid, tmp)
            mergesort(nums, mid + 1, end, tmp)
            merge(nums, start, end, mid, tmp)
        def merge(nums, start, end, mid, tmp):
            i, j = start, mid+1
            while i <= mid and j <= end:
                if nums[i] < nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            it, jt = start, mid+1
            while it <= mid and jt <= end:
                if nums[it] <= 2 * nums[jt]:
                    it += 1
                else:
                    self.cnt += mid - it + 1
                    jt += 1
            while i <= mid:
                tmp.append(nums[i])
                i += 1
            while j <= end:
                tmp.append(nums[j])
                j += 1
            nums[start: end+1] = tmp
            tmp.clear()
        mergesort(nums, 0, len(nums)-1, [])
        return self.cnt

