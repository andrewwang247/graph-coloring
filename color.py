"""
Check whether graph is colorable.

Copyright 2020. Siwei Wang.
"""
from typing import List
import click
from graph import Graph
# pylint: disable=no-value-for-parameter


def create_graph(filename: str) -> Graph:
    """Create graph from file."""
    num_edges = 0
    with open(filename) as fin:
        for line in fin:
            tokens: List[str] = line.strip().split()
            identifier = tokens[0]
            if identifier == 'c':
                continue
            if identifier == 'p':
                assert tokens[1] == 'color'
                assert len(tokens) == 4
                graph = Graph(int(tokens[2]))
                edges = int(tokens[3])
            elif identifier == 'e':
                assert len(tokens) == 3
                left = int(tokens[1])
                right = int(tokens[2])
                graph.add_edge(left, right)
                num_edges += 1
    assert edges == num_edges, 'Incorrect number of edges specified.'
    return graph


@click.command()
@click.option('--filename', '-f', required=True,
              type=click.Path(exists=True, file_okay=True,
                              dir_okay=False, readable=True),
              help='The file containing the graph specification.')
@click.option('--colors', '-c', required=True, type=int,
              help='The number of colors to use.')
@click.option('--useall', '-a', is_flag=True, default=False,
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
