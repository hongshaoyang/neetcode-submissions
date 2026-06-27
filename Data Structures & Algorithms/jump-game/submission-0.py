'''
- init
    - start = 0
    - max jump length = nums[i]
    - possible next jump lengths
    - get max and 


- try out forward greedy solution

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        
        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])
        return True
        