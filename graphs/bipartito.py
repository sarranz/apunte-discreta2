def bipartito(graph):
    """Determina si un grafo es bipartito. Si lo es, devuelve
    True y un coloreo de dos colores. Si no, False y un coloreo propio.
    """
    visited = []
    queue = []
    colouring = {}

    for r in graph.vertices():
        queue.append(r)
        visited.append(r)
        colouring[r] = 0

        while queue != []:
            v = queue.pop(0)
            for w in v.neighbours():
                if v not in visited:
                    visited.append(v)
                    queue.append(w)
                    colouring[w] = 1 - colouring[v]

    if is_proper(G, colouring):
        # El coloreo es propio.
        return True, colouring
    else:
        # El coloreo no es propio, coloreamos a cada vertice con un
        # color distinto.
        return False, {v:i for i,v in enumerate(graph.vertices())}
