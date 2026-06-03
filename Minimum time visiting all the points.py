class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            # The time to move between two points is the max of delta x and delta y
            total_time += max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
            
        return total_time

