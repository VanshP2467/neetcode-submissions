class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        
        for k, v in enumerate(nums):
            diff = target - v
            if diff in prevmap:
                return [prevmap[diff], k]
            prevmap[v] = k 
