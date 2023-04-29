import view as vw
import import_data as id
import export_data as ed
import work_data as wd

name_file = 'data.txt'

def button_click():
    num = vw.ViewMenu()
    data = id.Open_file(name_file)
    wd.init_data(data)
    match num:
        case 1:
            wd.print_note()
            view_data()
        case 2:
            wd.add_note()
            view_data()
        case 3:
            exit()
    quit()


 
def view_data():
    num = vw.WorkMenu()

    match num:
        case 1:
            wd.add_note()
        case 2:
            wd.search_note()
        case 3:
            wd.del_note()
        case 4:
            wd.print_note()
        case 5:
            exit()
    ed.Save_file(name_file, data, 'w')
    quit()