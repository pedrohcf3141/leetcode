# https://leetcode.com/problems/running-sum-of-1d-array/submissions//

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        lista = []
        for item in nums:
            sum += item
            lista.append(sum)
        return lista
