from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mydict:
                return [mydict[complement], i]
            mydict[nums[i]] = i
