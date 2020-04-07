def greedy(graph):
    colouring = {}
    # Utilizaremos a lo sumo colores 0, ..., Delta + 1.
    colours = range(graph.Delta() + 2)

    for v in graph.vertices():
        # Primero miramos los colores usados por los vecinos.
        # Notar que usamos .get(w) en lugar de [w], porque devuelve None
        # cuando w no esta coloreado.
        used = (colouring.get(w) for w in v.neighbours())

        # Y asignamos el minimo color no usado.
        colouring[v] = min(c for c in colours if c not in used)

    return colouring
