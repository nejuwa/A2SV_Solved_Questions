class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""] * len(s)
        for i, let in enumerate(s):
            indexed = indices[i]
            ans[indexed] = let
        return ''.join(ans)
