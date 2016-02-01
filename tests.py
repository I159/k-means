import math
import random
import unittest

import centroids
import clusters
import excp
import point
import space
import visualization


class PointsMixIn(unittest.TestCase):
    def setUp(self):
        self.points_number = 99
        self.points = list(self._points)

    @property
    def _points(self):
        lim = self.points_number
        while lim:
            lim = lim - 1
            yield point.Point(
                    x=random.gauss(mu=self.points_number/2,
                        sigma=self.points_number),
                    y=random.gauss(mu=self.points_number/2,
                        sigma=self.points_number))


class TestCluster(PointsMixIn):
    def setUp(self):
        super(TestCluster, self).setUp()
        self.cluster = clusters.Cluster(self.points[0])
        self.cluster.points = self.points

    def test_compute_centroid(self):
        old_centroid = self.cluster.centroid
        self.cluster.compute_centroid()
        self.assertNotEqual(old_centroid, self.cluster.centroid)
        self.assertFalse(self.cluster.compute_centroid())


class TestCentroid(PointsMixIn):

    def test_centroids(self):
        _centroids = centroids.get_initial_centroids(self.points, 10)
        self.assertEqual(len(_centroids), 10)
        self.assertTrue(isinstance(_centroids[0], point.Point))

    def test_too_much_centrods(self):
        self.assertRaises(excp.NotEnaughDataError,
                          centroids.get_initial_centroids,
                          self.points,
                          len(self.points)+1)


class TestPoint(PointsMixIn):
    def setUp(self):
        self.points_number = 2
        self.points = list(self._points)

    def test_point_sub(self):
        x_quadratic = pow(self.points[0].x - self.points[1].x, 2)
        y_quadratic = pow(self.points[0].y - self.points[1].y, 2)
        exp_dist = math.sqrt(x_quadratic + y_quadratic)
        dist = self.points[0] - self.points[1]
        self.assertEqual(dist, exp_dist)


class SpaceMixin(unittest.TestCase):
    def setUp(self):
        self.space = space.Space(999, 3)


class TestSpace(SpaceMixin):
    def test_stable_clusters(self):
        self.space.compute_stable_clusters()
        clusters = self.space.clusters
        for point in self.space.points:
            owner = min(clusters, key=lambda x: abs(x.centroid - point))
            self.assertIn(point, owner.points)

    def test_unique_points(self):
        self.space.compute_stable_clusters()
        clusters = self.space.clusters
        cl1, cl2, cl3 = map(lambda x: set(x.points), clusters)
        self.assertFalse(bool(cl1 & cl2 & cl3))

    def test_all_points(self):
        self.space.compute_stable_clusters()
        clusters = self.space.clusters
        self.assertEqual(sum((len(cl.points) for cl in clusters)),
                         len(self.space.points))


class TestVisualization(SpaceMixin):
    def test_vizualization(self):
        self.space.visualize_dynamic(delay=1)

    def test_static_visualization(self):
        self.space.vizualize()
