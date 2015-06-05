import centroids
import point


class NotEnaughDataError(Exception):
    """Not enough data.

    Raise if no data provided or a number of points lesser than required number
    of clusters."""
    pass


class Cluster(object):
    """Cluster object.

    Contains all cluster points."""


    def __init__(self, centroid):
        self.points = []
        self.centroid = centroid

    def recompute_centroid(self):
        """Recompute a centroid relying on a binded points coordinates."""

        import pdb; pdb.set_trace()

    def __repr__(self):
        return ('<{module}.{name} object at {hex_id}.'
                ' Centroid: {centroid} points number: {points}>').format(
                    module=self.__class__.__module__,
                    name=self.__class__.__name__,
                    hex_id=hex(id(self)),
                    centroid=self.centroid,
                    points=len(self.points))


def generate_clusters(num_points, num_clusters):
    if num_clusters > num_points:
        raise NotEnaughDataError(
                "Too few point for the given number of clusters:\n"
                " clusters: %s\n"
                " points: %s.")
    points = list(point.random_points(num_points))
    _centroids = centroids.get_initial_centroids(points, num_clusters)
    _clusters = [Cluster(i) for i in _centroids]
    for _point in points:
        # Find a closets to a point centroid and add the point to the centroid.
        min(((c, c.centroid - _point) for c in _clusters),
                key=lambda x: x[1])[0].points.append(_point)

    return _clusters
