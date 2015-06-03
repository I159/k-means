def gram_matrix(points):
    """Distance Gram matrix.

    Every object of the matrix contains two point and distance measure between
    these points. The matrix required to compute initial centroids."""

    for i in points:
        yield [(i, v, i - v) for v in points]



def get_centroids(points):
    import pdb; pdb.set_trace()
