"""
Test colorings for edgeless graphs.

Copyright 2020. Siwei Wang.
"""
from pytest import mark
from common import create_edgeless, parameters


@mark.parametrize('vertices,colors', parameters(7, 8))
def test_edgeless(vertices: int, colors: int):
    """Test edgeless graph colorings."""
    graph = create_edgeless(vertices)
    colorings = graph.colorings(colors)
    num_colorings = sum(1 for _ in colorings)
    assert num_colorings == colors ** vertices
