class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in image:
            r.reverse()
            for j in range(len(r)):
                if r[j] == 1:
                    r[j] = 0
                else:
                    r[j] = 1
        return image
