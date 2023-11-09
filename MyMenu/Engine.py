from MyMenu import MyMenu as menu
import Controller.Engine as eng


def menu():
    while True:
        menu.draw_menu()
        user_input = input()
        # if user_input == '1':
        #     print("all")
        # elif user_input == '2':
        #     print("ID")
        # elif user_input == '3':
        #     print("date")
        # elif user_input == '4':
        #     print("all")
        # elif user_input == '5':
        #     eng.add_note()
        # elif user_input == '6':
        #     print("all")
        # else:
        #     print("Программа Блокнот (Журнал заметок завершена)")
        match user_input:
            case 1:
                print('all')
            case 2:
                print('id')
            case 3:
                print('date')
            case 4:
                print('all')
            case 5:
                eng.add_note()
            case 6:
                print('all')
            case 7:
                print('Программа Блокнот (Журнал заметок) завершена')
                break
            case _:
                print('Введите номер пункта меню')

