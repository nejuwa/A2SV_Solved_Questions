class Solution:
    def frequencySort(self, s: str) -> str:
        ss= Counter(s)
        sorted_chars = sorted(ss.items(), key=lambda x: x[1], reverse=True)
        res= []
        for c, i in sorted_chars:
            res.append(i*c)
        return ''.join(res)
