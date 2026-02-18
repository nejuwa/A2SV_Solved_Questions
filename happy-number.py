class Solution:
    def isHappy(self, n: int) -> bool:
        see = set()
        while n != 1 and n not in see:
            see.add(n)
            s=0
            while n > 0:
                dig = n %10
                s += dig* dig
                n //=10
            n=s 
        return n ==1
