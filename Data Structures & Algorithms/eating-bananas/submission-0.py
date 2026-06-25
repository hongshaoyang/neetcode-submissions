'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1 
            elif nums[mid] == target:
                return mid
            else:
                hi = mid - 1
        return -1
'''


import math

class Solution:
    # min division size st
    # - # groups < h

    # min
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def groups(k):
            s = 0
            for p in piles:
                s += math.ceil(p / k)
            return s


        
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if groups(mid) > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo










        