class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        nn=set(nums)
        for i in range(len(nn)+1):
            if i not in nn:
                return i
