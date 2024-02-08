import graph

if __name__ == '__main__':
    e = graph.Edge('new')
    g = graph.Graph('test2')
    g = graph.load_graph('testGraph')
    g.add_edge(e)
    print(g)
