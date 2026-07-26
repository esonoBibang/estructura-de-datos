
#Tiempo constante --> O(1) — Tiempo constante
lista = [10,20,30,40,50,60]
print(lista[3])

#O(log n) — Tiempo logarítmico
def busqueda_binaria(lista_ordenada, objetivo):
    izquierda, derecha = 0, len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == objetivo:
            return medio #Valor encontrado
        elif lista_ordenada[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return f'No se encontro el indice'
print(busqueda_binaria(lista,20))


#O(n) lineal
def busqueda_lineal(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice
    return -1

# Ejemplo de uso
lista = [42, 5, 17, 23, 99, 8]
resultado = busqueda_lineal(lista, 23)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")

#O(n log n)
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
ordenada = merge_sort(lista)
print(ordenada)


#O(n^2)
def comparar_pares(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            print(f"Comparando {lista[i]} con {lista[j]}")

# Ejemplo de uso
datos = [3, 7, 2, 9]
comparar_pares(datos)