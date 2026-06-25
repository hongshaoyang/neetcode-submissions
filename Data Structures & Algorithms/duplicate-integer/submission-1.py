class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = dict()
        for i, e in enumerate(nums):
            if e in found:
                return True
            found[e] = 1
        return False

        