

# def func():
#
#     print('Minha primeira função.')
#
#
# func()
#
#
# def func_2():
#
#     num = int(input('Entre com número'))
#
#     print(num * 2)
#
#
# func_2()


def area_circunferia(raio: int):
    pi = 3.14

    print(f'A área da circ é {pi * raio ** 2}')

    return pi * raio ** 2


# area_circunferia(2)

area = area_circunferia(5)

print(area)


