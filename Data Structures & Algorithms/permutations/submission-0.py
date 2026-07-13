class Solution:
    '''
    1. basic recursion by building from N-1
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        first = nums[0]
        for p in self.permute(nums[1:]):

            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res
        