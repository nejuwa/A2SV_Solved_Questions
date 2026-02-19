class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num=nums[i+1: ]
            if target -nums[i] in num:
                return [nums.index(nums[i]), num.index(target -nums[i])+i+1]
                break
