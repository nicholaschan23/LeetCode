# Given an array nums. 
# We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        for i in range(0, len(nums)):
            results[i] = sum(nums[0:i+1])
        return results