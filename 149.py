# https://leetcode.com/problems/max-points-on-a-line/description/
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 1:
            return 1

        num = []
        for point1 in points:
            delta = dict()

            for point2 in points:
                deltax = point1.x - point2.x
                deltay = point1.y - point2.y

                if deltax == 0 and deltay == 0:
                    delta['SAME'] = delta.get('SAME', -1) + 1
                elif deltax == 0:
                    delta['NAN'] = delta.get('NAN', 0) + 1
                elif deltay/deltax == -0.0:
                    delta[0.0] = delta.get(0.0, 0) + 1
                elif abs(deltay) < abs(deltax):
                    delta[deltax/deltay] = delta.get(deltax/deltay, 0) + 1
                else:
                    delta[deltay/deltax] = delta.get(deltay/deltax, 0) + 1

            for key in delta:
                if key is 'SAME':
                    num.append(delta[key])
                    continue
                num.append(delta[key] + delta.get('SAME', 0))
        
        list.sort(num)
        if len(num) == 0:
            return 0

        return (num[-1] + 1)

test = Solution()

# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points1 = []
points1.append(Point(1, 1))
points1.append(Point(3, 2))
points1.append(Point(5, 3))
points1.append(Point(4, 1))
points1.append(Point(2, 3))
points1.append(Point(1, 4))
assert test.maxPoints(points1) == 4

# [[1,1],[2,2],[3,3]]
points2 = []
points2.append(Point(1, 1))
points2.append(Point(2, 2))
points2.append(Point(3, 3))
assert test.maxPoints(points2) == 3
