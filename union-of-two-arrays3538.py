class Solution:    
    def findUnion(self, a, b):
        # code here
        res=[]
        res.extend(set(a))
        for i in set(b):
            if i not in res:
                res.append(i)
        return res
            
