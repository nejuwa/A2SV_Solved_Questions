class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        arrow = 1
        last = points[0][1]

        for start, end in points:
            if start > last:   
                arrow += 1
                last = end    

        return arrow

