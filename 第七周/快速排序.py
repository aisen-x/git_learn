# 思路非常的清晰
def qiuck_sort(begin, end, nums):
    if begin > end:
        return
    middle_index = helper(begin, end, nums)
    qiuck_sort(begin, middle_index-1, nums)
    qiuck_sort(middle_index+1, end, nums)


def helper(left, right, nums):
    middle = nums[left]
    mark = left
    for i in range(left+1, right+1):
        if nums[i] > middle:
            mark += 1
            nums[i], nums[mark] = nums[mark], nums[i]
    nums[left], nums[mark] = nums[mark], nums[left]
    return mark
