class NotEnaughDataError(Exception):
    """Not enough data.

    Raise if no data provided or a number of points lesser than required number
    of clusters."""
    def __init__(self, clusters, points):
        msg = ("Too few points for the given number of clusters:\n"
               " clusters: {}\n"
               " points: {}".format(clusters, points))
        super(NotEnaughDataError, self).__init__(msg)
