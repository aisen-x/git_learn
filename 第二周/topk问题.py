import collections
import heapq
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        if k == 0 : return []
        res = collections.Counter(nums)
        heap = []
        for key, val in res.items():
            if len(heap) >= k:
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            heapq.heappush(heap, (val, key))
        ans = [item[1] for item in heap]
        return ans

