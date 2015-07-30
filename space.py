import random

import centroids
import clusters
import exceptions
import point
import visualization


def no_output_generator(f):
    """If you don't need a generator with all clusters conditions just call
    pass generator=False and just compute it."""

    def wrap(self, generator=True):
        out = f(self)
        if generator:
            return out
        for i in out:
            result = i
            return result
    return wrap


class Space(object):
    """Two dimensional space contains clustered random points.

    The most general object contains all the points and clusters. Performs
    clustering computations."""

    def __init__(self, num_points, num_clusters):
        self.points = list(self._random_points(num_points))
        self.num_clusters = num_clusters
        self.__clusters = None

        self.old_centroids = []

    def _random_points(self, points_number):
        """Get random unique points list of a given number of points.

        Generation of point coordinates with Gaussian Distribution guarantee
        points uniqueness and good deviation of points in a space."""
        lim = points_number
        while lim:
            lim = lim - 1
            yield point.Point(
                    x=random.gauss(mu=points_number/2, sigma=points_number),
                    y=random.gauss(mu=points_number/2, sigma=points_number))

    @property
    def clusters(self):
        if self.__clusters:
            return self.__clusters

        len_points = len(self.points)
        if self.num_clusters > len_points:
            raise excp.NotEnaughDataError(clusters, len_points)

        _centroids = centroids.get_initial_centroids(
                self.points, self.num_clusters)
        self.__clusters = [clusters.Cluster(i) for i in _centroids]
        return self.__clusters

    @no_output_generator
    def compute_stable_clusters(self):
        """Implemented as generator to track computation."""
        while any((i.compute_centroid() for i in self.clusters)):
            for cl in self.clusters:
                cl.points = []
            for _point in self.points:
                min(((c, c.centroid - _point) for c in self.clusters),
                        key=lambda x: x[1])[0].points.append(_point)
            yield self.clusters

    def visualize_dynamic(self, delay):
        plot = visualization.DynamicPlot(
              self.compute_stable_clusters())
        plot.visualize(delay=delay)

    def vizualize(self):
        plot = visualization.StaticPlot(
                self.compute_stable_clusters(False))
        plot.visualize()

