class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s=""
        siz = len(min(strs, key=lambda x: len(x)))
        for l in range(siz):
            char = strs[0][l]
            for c in strs:
                if c[l] != char:
                    return s                
            s += char
        return s
