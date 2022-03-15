f = int(input('Primeiro Bimestre: '))
g = int(input('Segundo Bimestre: '))
h = int(input('Terceiro Bimestre: '))
i = int(input('Quarto Bimestre: '))
med = (f + g + h + i) / 4

if f <= 10 and g <= 10 and h <= 10 and i <= 10:
    print('média: {}'.format(med))
else:
    print('Foi informada alguma nota errada')

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do programa')
#
# d = int(input('Entre com um valor: '))
# e = int(input('Entre outro valor: '))
# resto_d = d % 2
# resto_e = e % 2
#
# if resto_d == 0 or resto_e == 0:
#     print('Um número par foi digitado')
# else:
#     print('Não um número par')
