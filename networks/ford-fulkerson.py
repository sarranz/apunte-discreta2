def ford_fulkerson(network):
    """Devuelve un flujo maximal de s a t.

    Puede no terminar."""

    vertices, edges, capacity, s, t = network
    f = {edge: 0 for edge in edges}  # Flujo nulo.

    path = pick_non_saturated_path(network, f)
    while (path != []):
        # Calcular epsilon.
        epsilon = min(capacity(e) for e in path)

        # Aumentar f.
        for edge in path:
            f[edge] += epsilon

        path = pick_non_saturated_path(network, f)

    return f
