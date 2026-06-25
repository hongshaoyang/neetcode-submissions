class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers

        i, j = 0, len(numbers)-1

        while i < j:
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
            if nums[i] + nums[j] > target:
                j -= 1
            
            if nums[i] + nums[j] < target:
                i += 1

            

        return [0, 0]
        