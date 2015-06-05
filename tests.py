import itertools
import math
import unittest

import centroids
import clusters
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


class PointsMixIn(unittest.TestCase):
    """Initialize 100 random points."""
    def setUp(self):
        self.points = list(point.random_points(100))
        super(PointsMixIn, self).setUp()


class TestRandomPoinGenerator(PointsMixIn):
    """Test random points generation."""

    def test_points_number(self):
        """Test for correct generated points number."""
        self.assertEqual(len(self.points), 100)

    def test_unique(self):
        """Test for uniqueness.

        Test that a length of a points collection the same before and after
        removing of a duplicate points."""
        self.assertEquals(len(self.points), len(set(self.points)))


class TestCentroidsCalculation(PointsMixIn):
    """Test initial centroids calculation."""

    def test_initial_number(self):
        """Test for correct number of initialized centroids."""
        cnts = centroids.get_initial_centroids(self.points, 3)
        self.assertEquals(len(cnts), 3)

    def test_initial_unique(self):
        """Test for uniqueness."""
        cnts = centroids.get_initial_centroids(self.points, 3)
        self.assertEquals(len(cnts), len(set(cnts)))


class TestCluster(unittest.TestCase):
    """Test cluster computation."""

    def setUp(self):
        self.clusters = clusters.generate_clusters(999, 3)
        super(TestCluster, self).setUp()

    def test_initialize_clusters(self):
        """Test for proper number of points and cluster."""
        self.assertEquals(len(self.clusters), 3)
        self.assertEquals(len(
            list(itertools.chain(*(i.points for i in self.clusters)))), 999)

    def test_unique_initialize(self):
        """Test for points bind uniqueness."""
        binded_points = list(
                itertools.chain(*(i.points for i in self.clusters)))
        self.assertEquals(len(binded_points), len(set(binded_points)))
