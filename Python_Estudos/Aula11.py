# lista = [1, 10]
#
# try:
#     divisao = 10 / 1
#     numero = lista[1]
# except ZeroDivisionError:
#     print('Não é possivel realizar uma divisão por 0')
# except IndexError:
#     print('Erro ao acessar um indice invalido da lista')
# except BaseException as ex:
#     print(ex)
# else:
#     print('Executa quando não ocorre exceção')
# finally:
#     print('Sempre executa')
# # Utilizado para criar exceções e poder ajudar na resolução
# # de erros de resultado no uso do codigo

class Error(Exception):
    pass  # não faz nada so impede de dar um erro no codigo


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break  # força a parada do while
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)
