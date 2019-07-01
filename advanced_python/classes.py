import numpy as np
from numpy import linalg as la


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = np.array(p1)
        self.p2 = np.array(p2)
        self.p3 = np.array(p3)
        self.points = [self.p1, self.p2, self.p3]

    def area(self):
        """ It calculates the area by the cross product"""
        v1 = self.p2 - self.p1
        v2 = self.p3 - self.p1

        return la.norm(np.cross(v1, v2)) / 2

    def geometric_center(self):
        """ It calculates the mean of all the points"""
        return (self.p1 + self.p2 + self.p3) / 3

    @staticmethod
    def angle_between(v1, v2):
        """ We calculate the angle by calculating the cos, it returns the angle in degrees"""
        cos = float(np.dot(v1, v2)) / (la.norm(v1) * la.norm(v2))
        angle = np.round(np.arccos(cos) * (180 / np.pi), 2)
        return angle

    def angles(self):
        """ For each pair of points, we calculate the angle"""
        angles = []

        for (index, point) in enumerate(self.points):
            v1 = self.points[(index + 1) % 3] - point
            v2 = self.points[(index + 2) % 3] - point
            angle = self.angle_between(v1, v2)
            angles.append(angle)

        return angles

    def is_30_60_triangle(self):
        """ It checks if the angles are 30, 60, 90 """
        condition = len(set(self.angles()) - set([30.0, 60.0, 90.0])) == 0
        return condition

    def is_45_45_triangle(self):
        """ It checks if the angles are 45, 45, 90 """
        condition = len(set(self.angles()) - set([45.0, 45.0, 90.0])) == 0
        return condition

    def is_point_in_plane(self, point):
        """ We gonna check if the angle between the perpendicular vector and the point are 90"""
        v1 = self.p2 - self.p1
        v2 = self.p3 - self.p1
        v = point - self.p1

        perp_vector = np.cross(v1, v2)
        angle = self.angle_between(v, perp_vector)

        return angle == 90.0

    def normal(self):
        """ It calculates the normal vector defined by the cross product, with norm = 1 """
        v1 = self.p2 - self.p1
        v2 = self.p3 - self.p1

        return np.cross(v1, v2) / la.norm(np.cross(v1, v2))

    def is_same_area(self, other):
        return other.area() == self.area()

    @staticmethod
    def line_intersect(v1, v2, v3, v4):
        """ judge if line (v1,v2) intersects with line(v3,v4) """

        d = (v4[1] - v3[1]) * (v2[0] - v1[0]) - (v4[0] - v3[0]) * (v2[1] - v1[1])
        u = (v4[0] - v3[0]) * (v1[1] - v3[1]) - (v4[1] - v3[1]) * (v1[0] - v3[0])
        v = (v2[0] - v1[0]) * (v1[1] - v3[1]) - (v2[1] - v1[1]) * (v1[0] - v3[0])
        if d < 0:
            u, v, d = -u, -v, -d
        return (0 <= u <= d) and (0 <= v <= d)

    def is_overlapping(self, other):
        # First we need to check if they are in the same plane
        for point in self.points:
            if not other.is_point_in_plane(point):
                return False

        # Then we need to check if two sides of triangle A intersect with any side of triangle B
        intersections = 0
        for (index, (point, other_point)) in enumerate(zip(self.points, other.points)):
            if self.line_intersect(point, self.points[(index + 1) % 3], other_point, other.points[(index + 1) % 3]):
                intersections += 1

        return intersections >= 2

    def is_similar(self, other):
        """ They are similar if they have same angles """
        return len(set(self.angles()) - set(other.angles()))


t1 = Triangle((1, 2, 3), (2, 2, 3), (2, 1, 3))
t2 = Triangle((1, 2, 5), (2, 2, 5), (2, 1, 5))

assert t1.area() == 0.5
assert (t1.geometric_center() == [5 / 3, 5 / 3, 3]).all()
assert (t1.angles() == [45.0, 90.0, 45.0])
assert not t1.is_30_60_triangle()
assert t1.is_45_45_triangle()
assert t1.is_point_in_plane((0, 0, 3))
assert (t1.normal() == [0, 0, -1]).all()
assert t1.is_same_area(t2)
assert not t1.is_overlapping(t2)
assert not t1.is_similar(t2)
