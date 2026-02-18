class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ss= Counter(s)
        tt = Counter(t)
        if ss ==tt:
            return 0
        c=0
        for i in ss.keys():
            if ss[i] >= tt[i]:
                c+=abs(ss[i]-tt[i])
        return c
            
