def edmondskarp(network):
    vertices, edges, capacity, s, t = network
    f = {}

    while True:
        queue = [(s, None, None)]
        visited = set([s])
        i = 0

        # BFS searching augmenting paths.
        # queue stores (v, res_cap, w) where
        # v is a vertex added by w
        # and res_cap is the residual capacity of the edge.
        while t not in visited or len(queue) <= i:
            v, _, _ = queue[i]

            for w in v.neighboursf():
                # Forward neighbours.
                res_cap = capacity((v,w)) - f[(v,w)]
                if w not in visited and res_cap > 0:
                    queue.append((w, res_cap, v))
                    visited.add(w)

            for w in v.neighboursb():
                # Backward neighbours.
                res_cap = f[(w,v)]
                if w not in visited and res_cap > 0:
                    queue.append((w, res_cap, v))
                    visited.add(w)

            i += 1

        # Check if we found an augmenting path.
        if t not in visited:
            break

        # Reconstruct path and compute epsilon.
        path = []
        epsilon = queue[-1][1]

        while len(queue) > 1:
            w, res_cap, v = queue.pop()
            path.insert(0, w)
            epsilon = min(epsilon, res_cap)

            while queue[-1][0] != v:
                queue.pop()

        path.insert(0, s)

        # Increment f.
        for v, w in zip(path, path[1:]):
            if (v,w) in edges:
                f[(v,w)] += c
            else:
                f[(w,v)] -= c

    return f
