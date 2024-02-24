

d = {'a': 'oi', 'b': [1, 2, 3], 'c': 3}

print(d)
# print(type(d))

print(d['b'])

d['chave nova'] = 4

print(d)

del d['a']

print(d)

# print(d.items())

for chave, valor in d.items():

    print(chave, valor)

