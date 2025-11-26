import matplotlib.pyplot as plt
import numpy as np

def graficar_comparacion(pares, nodos_generados, nodos_visitados, tiempos):
    metodos = ['RyA', 'RyAsub']
    x = np.arange(len(pares))
    width = 0.35

    fig, axs = plt.subplots(3, 1, figsize=(10, 12))
    fig.suptitle('Comparación RyA vs RyAsub')

    # Nodos generados
    axs[0].bar(x - width/2, nodos_generados['RyA'], width, label='RyA')
    axs[0].bar(x + width/2, nodos_generados['RyAsub'], width, label='RyAsub')
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(pares)
    axs[0].set_ylabel("Nodos Generados")
    axs[0].legend()

    # Nodos visitados
    axs[1].bar(x - width/2, nodos_visitados['RyA'], width, label='RyA')
    axs[1].bar(x + width/2, nodos_visitados['RyAsub'], width, label='RyAsub')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(pares)
    axs[1].set_ylabel("Nodos Visitados")
    axs[1].legend()

    # Tiempo
    axs[2].bar(x - width/2, tiempos['RyA'], width, label='RyA')
    axs[2].bar(x + width/2, tiempos['RyAsub'], width, label='RyAsub')
    axs[2].set_xticks(x)
    axs[2].set_xticklabels(pares)
    axs[2].set_ylabel("Tiempo (s)")
    axs[2].legend()

    plt.show()
