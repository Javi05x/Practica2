import search
from visualizacion import graficar_comparacion


pares_ciudades = ['A->B', 'T->M', 'Z->D', 'A->Z']

nodos_generados = {'RyA': [], 'RyAsub': []}
nodos_visitados = {'RyA': [], 'RyAsub': []}
tiempos = {'RyA': [], 'RyAsub': []}

pares = [('A', 'B'), ('T', 'M'), ('Z', 'D'), ('A', 'Z')]


def mostrar_resultados(metodo, problema, nombre_metodo):
    solucion, gen, vis, tiempo = metodo(problema)
    ruta = [node.state for node in solucion.path()]
    coste = solucion.path_cost
    print(f"{nombre_metodo} Path: {ruta}")
    print(f"Coste total: {coste}")
    print(f"Nodos generados: {gen}")
    print(f"Nodos visitados: {vis}")
    print(f"Tiempo ejecucion: {tiempo:.6f} segundos")
    print("--------------------------------------------------------------------------")

    # Acumula los datos para la gráfica
    nodos_generados[nombre_metodo].append(gen)
    nodos_visitados[nombre_metodo].append(vis)
    tiempos[nombre_metodo].append(tiempo)


for inicial, meta in pares:
    problema = search.GPSProblem(inicial, meta, search.romania)
    mostrar_resultados(search.rya_graph_search, problema, 'RyA')
    mostrar_resultados(search.ryasub_graph_search, problema, 'RyAsub')

# Al final muestra la gráfica con todos los resultados
graficar_comparacion(pares_ciudades, nodos_generados, nodos_visitados, tiempos)
