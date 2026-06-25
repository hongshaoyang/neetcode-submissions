from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []

        for e, v in counter.items():
            heapq.heappush(heap, (v, e))
        
        res = []
        while len(heap) > k:
            heapq.heappop(heap)

    

        return [e[1] for e in heap]
