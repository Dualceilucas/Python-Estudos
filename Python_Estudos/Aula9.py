# arquivo = open('teste.txt', 'w')  # w = write: escreve na linha indicada e sobepoem se ja tiver algo escrito
# arquivo.write('Primeira linha')
# arquivo.close()
# arquivo = open('teste.txt', 'a')  # a: continua escrevendo na mesma linha sem sobrepor
# arquivo.write('\nSegunda linha')  # para passar pra proxima linha necessario colocar \n
# arquivo.close()
import shutil


def escrever_arquivo(texto):
    diretorio = 'C:/Users/dualc/Desktop/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')  # r = read: ler o arquivo informado
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')  # split - transforma o texto no arquivo em lista
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/dualc/Desktop/')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/dualc/Desktop/nota.txt')


if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = 'Cesar, 7, 9, 3, 8\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
