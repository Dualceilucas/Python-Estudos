lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
a = input('Digite o nome de um animal: ')

print(lista_animal[1])

if a in lista_animal:
    print('existe um {} na lista'.format(a))
else:
    print('Não existe um {} na lista. Será incluído'.format(a))
    lista_animal.append(a)
    print(lista_animal)

lista_animal.pop()
print(lista_animal)