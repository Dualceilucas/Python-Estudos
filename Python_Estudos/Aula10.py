from datetime import date, time, datetime, timedelta


def trab_comdatetime():
    date_atual = datetime.now()
    print(date_atual)
    print(date_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(date_atual.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo')
    print(tupla[date_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    nova_data = data_criada - timedelta(days=365)
    print(nova_data)


def trab_comdate():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y'))


def trab_comtime():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))


if __name__ == '__main__':
    # trab_comdate()
    # trab_comtime()
    trab_comdatetime()
