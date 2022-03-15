# for x in range(1,101):
#     print(x)

# a = int(input('Entre com um número: '))
# div = 0
#
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1  # (div += 1 ) é a mesma coisa
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))

# a = int(input('Entre com um valor: '))
#
# # for num in range(a+1):
# #     div = 0
# #     for x in range(1, num+1):
# #         resto = num % x
# #         if resto == 0:
# #             div = div + 1  # (div += 1 ) é a mesma coisa
# #     if div == 2:
# #         print(num)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Entre com a nota: '))
print('Sua nota foi {}'.format(nota))
