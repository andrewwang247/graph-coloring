"""
Test colorings for path graphs.

Copyright 2020. Siwei Wang.
"""
from pytest import mark
from common import parameters, create_path


@mark.parametrize('vertices,colors', parameters(7, 9, non_zero=True))
def test_path(vertices: int, colors: int):
    """Test path graph colorings."""
    graph = create_path(vertices)
    colorings = graph.colorings(colors)
    num_colorings = sum(1 for _ in colorings)
    assert num_colorings == colors * (colors - 1) ** (vertices - 1)
