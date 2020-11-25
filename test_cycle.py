"""
Test colorings for cycle graphs.

Copyright 2020. Siwei Wang.
"""
from pytest import mark
from common import parameters, create_cycle


def expected(vertices: int, colors: int) -> int:
    """Compute expected colorings with chromatic polynomial."""
    return (colors - 1)**vertices + (-1)**vertices * (colors - 1)


@mark.parametrize('vertices,colors', parameters(7, 9, non_zero=True))
def test_cycle(vertices: int, colors: int):
    """Test path cycle colorings."""
    graph = create_cycle(vertices)
    colorings = graph.colorings(colors)
    num_colorings = sum(1 for _ in colorings)
    assert num_colorings == expected(vertices, colors)
