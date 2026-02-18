class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res = Counter()
        for day in responses:
            unique_day = set(day)
            res.update(unique_day)
        
        maxx = 0
        result = ""
        for r in sorted(res.keys()):
            count = res[r]
            if count > maxx:
                maxx = count
                result = r
        return result
        
