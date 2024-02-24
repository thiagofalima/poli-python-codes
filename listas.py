

lista1 = [1, 2, 3, 4, 5, 6, 7]
#        [0, 1, 2, 3, 4, 5, 6]

print(lista1)

# print(type(lista1))

print(len(lista1))

print(lista1[0])
print(lista1[2])
print(lista1[3])
print(lista1[0: 3])
print(lista1[0: 3: 2])
print(lista1[-1])
print(lista1[0:])
print(lista1[:4])
print(lista1[::-1])

lista1[0] = 'valor alterado'

print(lista1)

lista1.append(8)

print(lista1)

lista2 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 54, 6, 6, 6, 6, 6,6 ]

print(lista2.count(3))

lista_mista = [1, 3.14, 'Oi', True]

print(lista_mista)