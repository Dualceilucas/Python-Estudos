# def soma(numero1, numero2):
#     return numero1 + numero2
#
#
# def subtracao(numero1, numero2):
#     return numero1 - numero2
#
#
# def multiplicacao(multiplicador, numero):
#     return multiplicador * numero
#
#
# def divisao(divisor, numero):
#     return numero / divisor

Calculadora = dict(soma=lambda a, b: a + b,
                   subtracao=lambda a, b: a - b,
                   multiplicacao=lambda a, b: a * b,
                   divisao=lambda a, b: b / a)

soma = Calculadora['soma']
subtracao = Calculadora['subtracao']
multiplicacao = Calculadora['multiplicacao']
divisao = Calculadora['divisao']


def ler_como_float():
    numero = input()
    return float(numero)


def menu():
    escolha = ''
    while escolha != '0':
        print('[1] Soma')
        print('[2] Subtração')
        print('[3] Multiplicação')
        print('[4] Divisão')
        print('[0] FINALIZAR PROGRAMA')

        escolha = input()
        if escolha == '1':
            print('Digite o primeiro número para soma')
            numero1 = ler_como_float()
            print('Digite o segundo número para soma')
            numero2 = ler_como_float()
            resultado = soma(numero1, numero2)
            print('O resultado da soma é {} '.format(resultado))

        if escolha == '2':
            print('Digite o primeiro número para substração')
            numero1 = ler_como_float()
            print('Digite o segundo número para substração')
            numero2 = ler_como_float()
            resultado = subtracao(numero1, numero2)
            print('O resultado da subtração é %s ' % resultado)

        if escolha == '3':
            print('Digite o multiplicador')
            multiplicador = ler_como_float()
            print('Digite o número que será multiplicado')
            numero = ler_como_float()
            resultado = multiplicacao(multiplicador, numero)
            print('O resultado da multiplicação é %s ' % resultado)

        if escolha == '4':
            print('Digite o divisor')
            divisor = ler_como_float()
            print('Digite o número que será dividido')
            numero = ler_como_float()
            resultado = divisao(divisor, numero)
            print('O resultado da divisão é %s ' % resultado)


menu()
