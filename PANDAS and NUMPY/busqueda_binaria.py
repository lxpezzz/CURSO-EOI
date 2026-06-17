# Asi se crea la búsqueda en binario,
# hay que tener en cuenta que la lista tiene que estar en orden
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

resultado = binary_search(lista, 6)
print(resultado)
