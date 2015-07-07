import centroids
import point


class Cluster(object):
    """Cluster object.

    Contains all cluster points and a centroid."""


    def __init__(self, centroid):
        self.points = []
        self.centroid = centroid
        self.__old_centroids = [self.centroid]

    def __repr__(self):
        return ('<{module}.{name} object at {hex_id}.'
                ' Centroid: {centroid} points number: {points}>').format(
                    module=self.__class__.__module__,
                    name=self.__class__.__name__,
                    hex_id=hex(id(self)),
                    centroid=self.centroid,
                    points=len(self.points))

    def compute_centroid(self):
        try:
            coord_sum = reduce(
                    lambda a, b: point.Point(a.x + b.x, a.y + b.y),
                    self.points)
            len_points = float(len(self.points))
            new_ctrd = point.Point(
                    coord_sum.x/len_points, coord_sum.y/len_points)
        except TypeError:
            return self.centroid

        if abs(self.centroid - new_ctrd) > 1 and\
                not new_ctrd in self.__old_centroids:
            self.__old_centroids.append(new_ctrd)
            self.centroid = new_ctrd
            return self.centroid

        return False
