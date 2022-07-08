"""

https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

"""


class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        dist = [[0] * n for i in range(n)]  # [[0] * n] * n will only create references to a shared list
        # print(dist)
        for i in range(n - 1):
            for j in range(i + 1, n):
                dist[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[j][i] = dist[i][j]
                # print("{0}: {1} <-> {2}: {3} ({4})".format(i, points[i], j, points[j], dist[i][j]))
        # print(dist)
        min_cost = 0
        inf = 10e7
        for i in range(n):
            min_dist = inf
            min_j = 0
            for j in range(n):
                if i != j and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    min_j = j
            dist[i][min_j] = inf
            dist[min_j][i] = inf
            print("{0} <-> {1}, min_dist = {2}, min_j = {3}".format(points[i], points[min_j], min_dist, min_j))
            min_cost += min_dist
        return min_cost


sol = Solution()
print(sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
