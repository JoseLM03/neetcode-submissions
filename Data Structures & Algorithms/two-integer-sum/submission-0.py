class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], index]
            else:
                dictionary[num] = index