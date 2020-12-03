"""
Graph representation as edge set.

Copyright 2020. Siwei Wang.
"""
from typing import Iterable, Set, Tuple
from itertools import product


def surjective_maps(domain_size: int,
                    codomain_size: int) \
        -> Iterable[Tuple[int, ...]]:
    """Construct all surjective maps [domain_size] -> [codomain_size]."""
    all_maps = product(range(codomain_size), repeat=domain_size)
    return filter(lambda func: len(set(func)) == codomain_size, all_maps)


class Graph:
    """Graph representation as edge set."""

    def __init__(self, vertices: int):
        """Initialize empty graph on given number of vertices."""
        self.num_vertices = vertices
        self.edge_set: Set[Tuple[int, int]] = set()

    def add_edge(self, vert_1: int, vert_2: int):
        """Add an edge between vertices 1 and 2."""
        assert 0 <= vert_1 < self.num_vertices, \
            f'Vertex {vert_1} is out of bounds.'
        assert 0 <= vert_2 < self.num_vertices, \
            f'Vertex {vert_2} is out of bounds.'
        self.edge_set.add((min(vert_1, vert_2), max(vert_1, vert_2)))

    def _is_proper_coloring(self, coloring: Tuple[int, ...]) -> bool:
        """Check whether the given coloring is proper."""
        return all(coloring[vert_1] != coloring[vert_2]
                   for vert_1, vert_2 in self.edge_set)

    def colorings(self, colors: int,
                  use_all: bool = False) -> Iterable[Tuple[int, ...]]:
        """Generate vertex colorings. Flag whether all colors must be used."""
        all_maps = product(range(colors), repeat=self.num_vertices)
        if use_all:
            all_maps = filter(lambda func: len(set(func)) == colors, all_maps)
        return filter(self._is_proper_coloring, all_maps)
