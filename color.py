"""
Check whether graph is colorable.

Copyright 2020. Siwei Wang.
"""
from typing import List
from click import command, option, Path
from graph import Graph
# pylint: disable=no-value-for-parameter


def create_graph(filename: str) -> Graph:
    """Create graph from file."""
    with open(filename, encoding='UTF-8') as fin:
        first_tokens: List[str] = fin.readline().strip().split()
        assert len(first_tokens) == 4
        assert first_tokens[0] == 'p'
        assert first_tokens[1] == 'color'
        graph = Graph(int(first_tokens[2]))
        edges = int(first_tokens[3])
        for line in fin:
            tokens: List[str] = line.strip().split()
            identifier = tokens[0]
            assert identifier in ('c', 'e'), \
                f'Unrecognized identifer: {identifier}'
            if identifier == 'e':
                assert len(tokens) == 3
                left = int(tokens[1])
                right = int(tokens[2])
                graph.add_edge(left, right)
    assert edges == len(graph.edge_set), \
        f'Expected {edges} edges, but got {len(graph.edge_set)}.'
    return graph


@command()
@option('--filename', '-f', required=True,
        type=Path(exists=True, file_okay=True,
                  dir_okay=False, readable=True),
        help='The file containing the graph specification.')
@option('--colors', '-c', required=True, type=int,
        help='The number of colors to use.')
@option('--useall', '-a', is_flag=True, default=False,
        help='Use at least one of each color. Off by default.')
def main(filename: str, colors: int, useall: bool):
    """Check whether graph is colorable."""
    assert colors > 0, 'Requires at least 1 color.'
    graph = create_graph(filename)
    num_vertices = graph.num_vertices
    num_edges = len(graph.edge_set)
    print(f'Graph with {num_vertices} vertices, {num_edges} edges.')
    for vert_1, vert_2 in graph.edge_set:
        print(f'{{{vert_1}, {vert_2}}}')
    colorings = graph.colorings(colors, useall)
    print(f'\nThere are {sum(1 for _ in colorings)} {colors}-colorings.')


if __name__ == '__main__':
    main()
