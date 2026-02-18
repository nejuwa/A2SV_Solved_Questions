class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res=[]
        if num %3 != 0:
            return res
        else:
            res.append(num//3 -1)
            res.append(num//3)
            res.append(num//3 + 1)
            return res
