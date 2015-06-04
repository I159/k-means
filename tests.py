import math
import unittest

import centroids
import point


class TestPoint(unittest.TestCase):
    """Test `Point` functionality."""

    def test_assigment(self):
        """Test point coordinates assignment."""
        new_point = point.Point(x=1.5, y=2.3)
        self.assertEquals((new_point.x, new_point.y), (1.5, 2.3))

    def test_measure(self):
        """Test points distance measure calculation."""
        point1 = point.Point(x=2, y=3)
        point2 = point.Point(x=4, y=5)

        euclidean = lambda a, b: math.sqrt(
                pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))
        self.assertEquals(point1-point2, euclidean((2, 3), (4, 5)))


class TestRandompoinGenerator(unittest.TestCase):
    """Test random points generation."""

    def test_points_number(self):
        """Test for correct generated points number."""
        self.assertEqual(len(list(point.random_points(10))), 10)

    def test_unique(self):
        """Test for uniqueness.

        Test that a length of a points collection the same before and after
        removing of a duplicate points."""
        points = list(point.random_points(1000))
        self.assertEquals(len(points), len(set(points)))



class TestCentroidsCalculation(unittest.TestCase):
    """"""
    def test_initial_number(self):
        points = list(point.random_points(100))
        cnts = centroids.get_initial_centroids(points, 3)
        self.assertEquals(len(cnts), 3)

    def test_initial_unique(self):
        points = list(point.random_points(100))
        cnts = centroids.get_initial_centroids(points, 3)
        self.assertEquals(len(cnts), len(set(cnts)))


