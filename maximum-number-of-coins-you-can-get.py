class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        s=0
        l=len(piles)//3
        a=1
        for i in range(l):
            s+=piles[i+a]
            a+=1
        return s
