class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num =Counter(nums)
        res=[]
        a=saorted(num.items(), key=lambda x: x[1], reverse =True)
        for i in range(k):
            res.append(a[i][0])
        return res
