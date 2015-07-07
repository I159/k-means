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
