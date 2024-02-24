
# nome = input('Entre com seu nome: ').title()
#
# if len(nome) > 5:
#     print(len(nome))
#     print(f'{nome} tem mais de 5 letras.')
#
# if nome == 'Thiago':
#     print(f'Bem-vindo {nome}')
#
# else:
#     print(len(nome))
#     print(f'{nome} tem menos de 5 letras')


num = int(input('Entre com um número: '))

if num > 0:

    if num % 2 == 0:

        print(f'{num} é par.')

    else:

        print(f'{num} é ímpar')

else:

    print(f'{num} não é maior que zero.')
