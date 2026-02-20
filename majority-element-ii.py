class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        fre = len(nums)/3
        c = Counter(nums)
        res=[]
        for i in c.keys():
            if c[i] > fre:
                res.append(i)
        return res
