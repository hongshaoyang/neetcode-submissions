class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid == 0 and nums[0] < nums[-1]:
                return nums[mid]
            if nums[mid] > nums[hi]:
                # search right
                lo = mid + 1
            if nums[mid] < nums[hi]:
                # search left
                hi = mid
        return nums[lo]