class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c= Counter(nums)
        for i in c.keys():
            if c[i]==1:
                return i


