class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid == 0 and nums[0] < nums[-1]:
                lo = mid # dunno if this is needed
                break
            if nums[mid] > nums[hi]:
                # search right
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                # search left
                hi = mid

        # lo is the pivot (minimum in nums)
        pivot = lo

        if target >= nums[0] and pivot != 0:
            lo, hi = 0, pivot-1
        else:
            lo, hi = pivot, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                hi = mid - 1
        return -1