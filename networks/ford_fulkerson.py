def ford_fulkerson(network):
    """Devuelve un flujo maximal de s a t."""

    vertices, edges, capacity, s, t = network
    f = {edge: 0 for edge in edges}  # Flujo nulo.

    path = pick_augmenting_path(network, f)
    while (path != []):
        def epsilon_i(edge):
            """El epsilon de un lado cambia si
            es forward o backward. Si es backward, f(xy)
            no esta definido, pero f(yx) si."""
            if edge.forward():
                return capacity(edge) - f(edge)
            else:
                return f(edge.invert())

        # Calcular epsilon.
        epsilon = min(epsilon_i(edge) for edge in path)

        # Aumentar f.
        for edge in path:
            if edge.forward():
                f[edge] += epsilon
            else:
                f[edge] -= epsilon

        path = pick_augmenting_path(network, f)

    return f
