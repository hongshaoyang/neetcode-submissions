
'''
- heapify in O(N)
- while there are stones remaining: O(N)
    - pop heaviest stone - O(logN)
    - pop 2nd heaviest stone - O(logN)
    - insert new stone - O(logN)
'''

import heapq # min heap

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap_neg = [-s for s in stones] # todo check model ans

        heapq.heapify(min_heap_neg)
    
        while len(min_heap_neg) > 1:
            s1 = -(heapq.heappop(min_heap_neg))
            s2 = -(heapq.heappop(min_heap_neg))

            if s1 == s2:
                continue
            
            heapq.heappush(min_heap_neg, -abs(s1-s2))

        if len(min_heap_neg) == 0:
            return 0

        return -min_heap_neg[0]




        