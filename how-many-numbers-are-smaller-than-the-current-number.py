class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=sorted(nums)
        res={}
        for i in range(len(n)):
            if n[i] not in res:
                res[n[i]] = i
            
        return [res[n] for n in nums]
            
