from collections import namedtuple
import random
import math

import point


class Point(namedtuple('Point', ('x', 'y'))):
    """Base point object.

    Store a point coordinates as `x` and `y` attributes. Compute Euclidean
    distance between two points using `-` operator."""

    def __sub__(self, other):
        """Return Euclidean distance between two points."""
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))


def random_points(points_number):
    """Get random unique points list of a given number of points.

    Generation of point coordinates with Gaussian Distribution guarantee
    points uniqueness and good deviation of points in a space."""
    lim = points_number
    while lim:
        lim = lim - 1
        yield point.Point(
                x=random.gauss(mu=points_number/2, sigma=points_number),
                y=random.gauss(mu=points_number/2, sigma=points_number))
