class Nodo:
    def __init__(self, simbolo, peso):
        self.simbolo = simbolo
        self.peso = peso
        self.der = None
        self.izq = None
        self.padre = None

def actualiza_arbol(frec):
    """hace el arbol de acuerdo a las frecuencias
    regresa la raiz del arbol
    """



def obtiene_hojas(nodos):
    """obtiene las hojas del arbol, recibe como entrada toda la lista de nodos"""


def recorrer(padre, lista_nodos, lista_pesos):
    """Se hace un recorrido infijo del arbol binario"""
    if padre != None:
        recorrer(padre.izq, lista_nodos, lista_pesos)
        lista_nodos.append(padre)
        lista_pesos.append(padre.peso)
        recorrer(padre.der, lista_nodos, lista_pesos)
    return lista_nodos, lista_pesos

def frecuencia(frase, frec):
    """obtiene la frecuencia de los simbolos en la frase"""

def leer_texto():
    texto = input("Escribe la frase que deseas codificar")
    return texto



def main():
    texto = leer_texto()

main()