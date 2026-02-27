class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sums = 0
        l = 0
        r=2
        while r< len(nums):
            a,b,c = nums[l], nums[l+1], nums[r]
            if a+b>c:
                sums = max(sums, a+b+c)
            l+=1
            r+=1
        return sums
