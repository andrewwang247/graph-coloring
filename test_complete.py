"""
Test colorings for complete graph.

Copyright 2020. Siwei Wang.
"""
from functools import reduce
from operator import mul
from pytest import mark
from common import create_kn, parameters, len_iter, check_surjective


def expected(vertices: int, colors: int) -> int:
    """Compute expected colorings with chromatic polynomial."""
    if vertices == 0:
        return 1
    return reduce(mul, (colors - k for k in range(vertices)))


@mark.parametrize('vertices,colors', parameters(6, 9))
def test_complete(vertices: int, colors: int):
    """Test complete graph colorings."""
    graph = create_kn(vertices)
    colorings = graph.colorings(colors)
    num_colorings = len_iter(colorings)
    assert num_colorings == expected(vertices, colors)
    assert check_surjective(graph, colors, num_colorings)
