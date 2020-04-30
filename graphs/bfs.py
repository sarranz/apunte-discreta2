def bfs(graph):
    visited = set()
    queue = []

    for r in graph.vertices():
        if r not in visited:
            queue.append(r)
            visited.add(r)

            while queue != []:
                v = queue.pop(0)
                for w in v.neighbours():
                    if w not in visited:
                        visited.add(w)
                        queue.append(w)

    return visited
