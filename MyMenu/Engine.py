from MyMenu import MyMenu as menu
import Controller.Engine as eng


def start():
    while True:
        menu.draw_menu()
        user_input = input()
        if user_input == '1':
            print("all")
        elif user_input == '2':
            print("ID")
        elif user_input == '3':
            print("date")
        elif user_input == '4':
            print("all")
        elif user_input == '5':
            eng.add_note()
        elif user_input == '6':
            print("all")
        else:
            print("Программа Блокнот (Журнал заметок завершена)")
            break

