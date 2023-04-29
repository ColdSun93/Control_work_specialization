import datetime

data = {}
id = 0


def write_data(data):
    global id
    heading = (input('Введите заголовок '))
    note = (input('Введите текст '))
    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data[id] = {'Heading': heading,
                'Note': note,
                'Date': date_now}
    print_note(data)
    return data


def add_note(data):
    global id
    if len(data) == 0:
        max_id = 0
    else:
        max_id = max(data.keys())

    id = int(max_id) + 1
    return write_data(data)


def del_note(data):
    data.pop(id)
    return data


def edit_note(data):
    global id
    id = (input('Введите номер записи '))
    for key_id in data.keys():
        if key_id == id:
            return write_data(data), print('Запись изменена')
            # print('Запись изменена')
        else:
            print('Искомая запись отсутствует')
    
    return data


def print_note(data):
    global id
    result = ''
    for keys, values in data[id].items():
        result = result + keys + ': ' + values + '; '
    print(f'id={id}, {result}')


def print_all_notes(data):
    for key_id in data.keys():
        result = ''
        for keys, values in data[key_id].items():
            result = result + keys + ': ' + values + '; '
        print(f'id={key_id}, {result}')
