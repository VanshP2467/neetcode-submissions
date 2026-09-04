class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for idx, val in enumerate(nums):
            diff = target - val 
            if diff in prevmap:
                return [prevmap[diff], idx]
            prevmap[val] = idx
