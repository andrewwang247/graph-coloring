"""
Common utilities for testing.

Copyright 2020. Siwei Wang.
"""
from typing import Iterable, Tuple, List
from math import comb
from itertools import product
from graph import Graph


def len_iter(iterable: Iterable) -> int:
    """Count number of entries in iterable."""
    return sum(1 for _ in iterable)


def check_surjective(graph: Graph, colors: int, num_colorings: int) -> bool:
    """Apply the relation between surjective colorings."""
    num_surjective = sum(comb(colors, sub_colors)
                         * len_iter(graph.colorings(sub_colors, True))
                         for sub_colors in range(colors + 1))
    return num_colorings == num_surjective


def parameters(vertex_max: int, color_max: int, non_zero: bool = False) \
        -> List[Tuple[int, int]]:
    """Create parameter list of all combinations."""
    return list(product(range(1 if non_zero else 0, vertex_max + 1),
                        range(color_max + 1)))


def create_kn(vertices: int) -> Graph:
    """Generate graph K_n."""
    graph = Graph(vertices)
    for i in range(vertices):
        for j in range(i + 1, vertices):
            graph.add_edge(i, j)
    return graph


def create_edgeless(vertices: int) -> Graph:
    """Create an edgeless graph with specified vertices."""
    return Graph(vertices)


def create_path(vertices: int) -> Graph:
    """Generate path graph P_n."""
    graph = Graph(vertices)
    for i, j in zip(range(vertices), range(1, vertices)):
        graph.add_edge(i, j)
    return graph


def create_cycle(vertices: int) -> Graph:
    """Generate cycle graph C_n."""
    graph = create_path(vertices)
    graph.add_edge(0, vertices - 1)
    return graph
