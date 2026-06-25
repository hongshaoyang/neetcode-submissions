class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {3: 0, ...} # compl: idx pair
        compl = {}
        for i, n in enumerate(nums):
            if (target - n) in compl:
                j = compl[(target - n)]
                return [j, i] # j is the smaller index
            compl[n] = i
        
        