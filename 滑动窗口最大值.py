import collections
class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j  in zip(range(1-k, n+1-k), range(n)):
            # 删除队列中对应的num(i-1)
            if i > 0 and deque[0] == nums[i-1]:
                deque.popleft()
            # 让队列保持递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i >= 0 and deque:
                res.append(deque[0])
        return res







