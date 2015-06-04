import itertools


def _gram_matrix(points):
    """Distance Gram matrix.

    Every object of the matrix contains two point and distance measure between
    these points. The matrix required to compute initial centroids."""

    for i in points:
        yield [(i, v, i - v) for v in points]


def _get_two_centroids(distances):
    """Get two points with the maximum distance between them.

    Take not just random centroids, instead of it we take two points with the
    maximum distance between them in accordance with K-Means++ algorithm."""

    key = lambda x: x[2]
    return list(max([max(i, key=key) for i in distances], key=key)[:2])


def _get_next_centroid(distances, centroids):
    """Get a point with the maximum distance from existing centroids.

    Choose a point with the maximum distance from a point among existing
    centroids."""

    target_measures = itertools.chain(
            *[i for i in distances if i[0][0] in centroids])
    next_centroid = max([i for i in target_measures if i not in centroids],
            key=lambda x: x[2])[2]
    return next_centroid


def get_initial_centroids(points, c_number=2):
    """Get a given number of centroids from existing points."""

    distances = list(_gram_matrix(points))
    exst_centroids = _get_two_centroids(distances)
    if c_number <= 2:
        return exst_centroids
    else:
        for i in range(c_number-2):
            exst_centroids.append(
                    _get_next_centroid(distances, exst_centroids))
    return exst_centroids
