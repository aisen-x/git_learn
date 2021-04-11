import heapq

class Solution:
    def getLeastNumbers(self, arr: [int], k: int) -> [int]:
        if k == 0: return []
        res = [-x for x in arr[: k]]
        heapq.heapify(res)
        for i in range(k, len(arr)):
            if -res[0] > arr[i]:
                heapq.heappop(res)
                heapq.heappush(res, -arr[i])
        hp = [-x for x in res]
        return hp


