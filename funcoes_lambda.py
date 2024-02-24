

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_quadrados = list(map(lambda x: x ** 2, lista))

print(lista_quadrados)

lista_pares = list(filter(lambda x: x % 2 == 0, lista))

print(lista_pares)

