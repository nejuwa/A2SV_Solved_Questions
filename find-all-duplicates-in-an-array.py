class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        c=Counter(nums)
        for i in c.keys():
            if c[i]==2:
                res.append(i)
        return res
