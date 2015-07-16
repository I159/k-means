import random

import excp


def get_initial_centroids(points, c_number):
    """Get a given number of centroids from existing points."""
    if len(points) < c_number:
        raise excp.NotEnaughDataError(c_number, len(points))
    return [points[random.randrange(len(points)-1)] for i in range(c_number)]
