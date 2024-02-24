
# nome = input('Entre com seu nome: ').title()
#
# if nome == 'Thiago':
#     print(f'Bem-vindo {nome}')
#
# elif len(nome) > 5:
#     print(len(nome))
#     print(f'{nome} tem mais de 5 letras.')
#
# elif nome == '':
#
#     print('Você não digitou nome algum.')
#
# else:
#     print(len(nome))
#     print(f'{nome} tem menos de 5 letras')


print('Programa para verificar se um ano é bissexto ou não.')

ano = int(input('Entre com o ano: '))

if ano % 400 == 0:

    print(f'{ano} é bissexto.')

elif ano == 2015:

    print(f'{ano} foi muito bom.')

else:

    print(f'{ano} não é bissexto.')

    



