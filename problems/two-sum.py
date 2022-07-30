# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        for x_index, x in enumerate(nums):
            for y_index, y in enumerate(nums):
                if x + y == target and x_index != y_index:
                    return [x_index, y_index]
        return 0
