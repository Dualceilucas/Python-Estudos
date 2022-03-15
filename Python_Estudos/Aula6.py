conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferença = conjunto.difference(conjunto2)
print(conjunto_diferença)
conjunto_difsimetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_difsimetrica)

lista = [1, 1, 2, 2, 3]
conjunto_numeros = set(lista)
print(conjunto_numeros)
lista_numeros = list(conjunto_numeros)
print(lista_numeros)

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)
