#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        aa=Counter(a)
        bb=Counter(b)
        # Your code here
        for i in bb:
            if bb[i] > aa[i]:
                return False
        return True
    
    
    
    
