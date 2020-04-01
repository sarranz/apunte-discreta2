def bfs(graph):
    visited = []
    queue = []

    for r in graph.vertices():
        queue.append(r)
        visited.append(r)

        while queue != []:
            v = queue.pop(0)
            if v not in visited:
                visited.append(v)
                for w in v.neighbours():
                    queue.append(w)

    return visited
