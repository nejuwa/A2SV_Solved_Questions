class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans=0
        ranges.sort()
        for i in range(left, right+1): 
            chek =False
            for l,r in ranges:
                if l <= i <=r:
                    chek =True
            if not chek:
                return False
            
        return chek
        
                
