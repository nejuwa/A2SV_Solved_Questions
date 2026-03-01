class Solution:
    def customSortString(self, order: str, s: str) -> str: 
        cnt = Counter(s)
        res = []
        for c in order:
            res.append(c * cnt[c])
            cnt[c] = 0
        for c in cnt:
            res.append(c * cnt[c])

        return "".join(res)
