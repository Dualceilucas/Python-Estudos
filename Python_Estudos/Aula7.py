class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aume_canal(self):
        if self.ligada:
            self.canal += 1

    def dimi_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.aume_canal()
    televisao.aume_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.dimi_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))


# class Calculadora:
#     def __init__(self, n1, n2):
#         self.a = n1
#         self.b = n2
#
#     def soma(self):
#         return self.a + self.b
#
#     def subtr(self):
#         return self.a - self.b
#
#
# calculadora = Calculadora(10, 2)
# print(calculadora.a)
# print(calculadora.soma())
# print(calculadora.subtr())
