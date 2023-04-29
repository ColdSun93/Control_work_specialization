import view as vw
import import_data as id
import export_data as ed
import work_data as wd

name_file = 'data.txt'

def button_click():
    data = {}
    num = vw.ViewMenu()
    match num:
        case 1:
            data = id.Open_file(name_file)
            wd.print_all_notes(data)

        case 2:
            data = wd.write_data(data)

        case 3:
            exit()
    view_data(data)



 
def view_data(data):
    num = vw.WorkMenu()

    match num:
        case 1:
            data = wd.add_note(data)
        case 2:
            data = wd.edit_note(data)
        case 3:
            data = wd.del_note()
        case 4:
            wd.print_all_notes(data)
        case 5:
            exit()
    view_quit(data)



def view_quit(data):
    num = vw.ViewWrite()
    match num:
        case 1:
            ed.Save_file(name_file, data, 'w')
        case 2:
            view_data(data)
        case 3:
            exit()

