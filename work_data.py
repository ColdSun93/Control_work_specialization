import datetime

data = {}
id = 1


def init_data(data_note):
    data = data_note
    global id


def write_data():

    heading = (input('Введите заголовок '))
    note = (input('Введите текст '))
    date_now = datetime.datetime.now()
    data[id] = {'Heading': heading,
                'Note': note,
                'Date': date_now}

    return data


def add_note():
    max_id = max(data.keys())
    id = max_id + 1
    write_data()



def search_note():
    id = (input('Введите номер записи '))
    for k in data.keys():
        if k == id:
            print_note()
        else:
            print('Искомая запись отсутствует')


def del_note():
    return data


def edit_note():
    id = (input('Введите номер записи '))
    for k in data.keys():
        if k == id:
            write_data()
        else:
            print('Искомая запись отсутствует')


def print_note():
    for keys, values in data[id].items():
        print('id: '+ id + keys + values)
        print('')
