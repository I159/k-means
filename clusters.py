import collections


class Cluster(collections.namedtuple("Cluster", ('centroid', 'points'))):
    def recompute_centroid(self):
        """Recompute a centroid relying on a binded points coordinates."""

        pass
