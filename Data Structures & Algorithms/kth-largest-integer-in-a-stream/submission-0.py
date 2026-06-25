class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for e in nums:
            self.add(e)
        

    def add(self, val: int) -> int:
        # always push then pop for top k 
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0] # peek at kth largest


        
