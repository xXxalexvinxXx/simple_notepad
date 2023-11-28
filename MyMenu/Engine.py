import MyMenu.MyMenu as menu
import Controller.Engine as engine


def start():
    while True:
        menu.draw_menu()
        user_input = input()
        if user_input == '1':
            engine.show('all')
        elif user_input == '2':
            engine.show('ID')
        elif user_input == '3':
            engine.show('date')
        elif user_input == '4':
            engine.show('all')
            engine.change_note()
        elif user_input == '5':
            engine.add_note()
        elif user_input == '6':
            engine.show('all')
            engine.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break

