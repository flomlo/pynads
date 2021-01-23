"""Implementation of the python API for the nads_count of the nads C++ library."""

from ._utils import _extract_unweighted_graph
from .nads_bind import compute_nads


def nads(adjacency_matrix, directed=True, min_dimension=1, max_dimension=-1):
    """
    Compute the number of almost-d-simplices of a given directed graph.

    Almost-d-simplices are tripels (s,s',e) where s,s' are two different (d-1)-simplices sharing
    a common (d-2)-dimensional face, e is a tupel (e1,e2) representing the edge needed to complete
    an almonst-d-simplex to a regular 'completed' d-simplex.


    Parameters
    ----------
    adjacency_matrix : 2d ndarray or scipy.sparse matrix, required
        Adjacency matrix of a directed/undirected unweighted graph. It is
        understood as a boolean matrix. Off-diagonal, ``0`` or ``False`` values
        denote absent edges while non-``0`` or ``True`` values denote edges
        which are present. Diagonal values are ignored. Must have at least one edge.

    directed : bool, optional, default: ``True``
        If ``True``, computes homology for the directed flag complex determined
        by `adjacency_matrix`. If ``False``, computes homology for the
        undirected flag complex obtained by considering all edges as
        undirected, and it is therefore sufficient (but not necessary)
        to pass an upper-triangular matrix.

    min_dimension: int, optional, default: ``2``
        Minimum dimension d of which to count the almost-d-simplices. 
        Must be greater or equal to 2, as ads for d=1 or d=2 are not defined.

    max_dimension: int, optional, default: ``-1``
        Maximum dimension d of which to count the almost-d-simplices. 
        If not set, the computation will go on until there are no more ads (and thus no more simplices).
        

    Returns
    -------
    out : list of int
        Number of almost-d-simplices, per dim d: min_dimension <= d <= max_dimension.

        to `min_dimension` and less than or equal to `max_dimension`.

    Notes
    -----
    The input graphs cannot contain self-loops, i.e. edges that start and end
    in the same vertex, therefore diagonal elements of the input adjacency
    matrix will be ignored.

    References
    ----------
    .. [1] TBA: nads.

    """
    # Extract vertices and edges
    vertices, edges = _extract_unweighted_graph(adjacency_matrix)

    assert(edges.size > 0)

    # Call nads binding
    res = compute_nads(vertices, edges, directed, min_dimension, max_dimension)

    return res

