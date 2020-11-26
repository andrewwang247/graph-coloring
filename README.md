# Graph Coloring

Enumeration of proper vertex colorings on an undirected graph.

```text
Usage: color.py [OPTIONS]

  Check whether graph is colorable.

Options:
  -f, --filename FILE   The file containing the graph specification.
                        [required]

  -c, --colors INTEGER  The number of colors to use.  [required]
  -a, --useall          Use at least one of each color. Off by default.
  --help                Show this message and exit.
```

The graph is internally represented as an edge set.

## File format

Graph file should be in [DIMACS format](http://lcs.ios.ac.cn/~caisw/Resource/about_DIMACS_graph_format.txt) for undirected graphs. Nodes are number from 0 up to `num_vertices` - 1.

```text
c This is a comment line. They being with c.
c The next line declares 4 vertices and 3 edges.
p color 4 3
c Each line afterward should start with e to describe edges.
e 0 1
e 1 3
e 2 1
```

## Example

Saving this information into a file `tmp.txt`, we then execute the coloring program.

```test
$ python3 color.py -f tmp.txt -c 5
Graph with 4 vertices, 3 edges.
{0, 1}
{1, 3}
{1, 2}

There are 320 5-colorings.
```

You can iterate through the colorings themselves with `Graph.colorings`.

## Testing

Run `pytest` for a series of parametrized unit tests for complete, cycle, edgeless, and path graphs. Validity is checked using [chromatic polynomials](https://en.wikipedia.org/wiki/Chromatic_polynomial).
