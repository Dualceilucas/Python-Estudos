# from Aula7 import Televisao
#
# if __name__ == '__main__':
#     televisao = Televisao()
#     print(televisao.ligada)
#     televisao.power()
#     print(televisao.ligada)

# def cont_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador
#
#
# if __name__ == '__main__':
#     lista = ['cachorro', 'gato', 'elefante']
#     print(cont_letras(lista))

cont_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']
print(cont_letras(lista_animais))

soma = lambda a, b:  a + b
print(soma(5, 10))
