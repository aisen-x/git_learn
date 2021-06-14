# 分治的思想

def mergesort(left, right, nums):
    if left > right:
        return
    # 位运算对半分
    mid = (left + right) >> 1
    mergesort(left, mid, nums)
    mergesort(mid+1, right, nums)
    merge(left, right, mid, nums)

def merge(left, right, mid, nums):
    tmp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if nums[i] > nums[j]:
            tmp.append(nums[i])
            i += 1
        if nums[i] <= nums[i]:
            tmp.append(nums[j])
    while i <= mid:
        tmp.append(nums[i])
    while j <= right:
        tmp.append(nums[j])
    nums[left: right+1] = tmp
