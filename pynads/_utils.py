"""Utility functions for adjacency matrices."""

import warnings

import numpy as np


def _extract_unweighted_graph(adjacency_matrix):
    input_shape = adjacency_matrix.shape
    # Warn if dense and not square
    if isinstance(adjacency_matrix, np.ndarray) and \
            (input_shape[0] != input_shape[1]):
        warnings.warn("Dense `adjacency_matrix` should be square.")

    # Extract vertices and give them weight one
    n_vertices = max(input_shape)
    vertices = np.ones(n_vertices, dtype=np.float)

    # Extract edge indices
    if isinstance(adjacency_matrix, np.ndarray):
        # Off-diagonal mask
        mask = np.logical_not(np.eye(input_shape[0], M=input_shape[1],
                                     dtype=bool))

        # Data mask
        mask = np.logical_and(adjacency_matrix, mask)

        edges = np.argwhere(mask)
    else:
        edges = np.argwhere(adjacency_matrix)

        # Remove diagonal elements a posteriori
        edges = edges[edges[:, 0] != edges[:, 1]]

    # Assign weight one
    edges = np.insert(edges, 2, 1, axis=1)

    return vertices, edges
