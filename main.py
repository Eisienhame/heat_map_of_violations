from utils import import_csv_data, into_dict, build_graph, into_dict_top10
from pathlib import Path


menu_exit = True

while menu_exit:
    print("Здравствуйте, напишите полный путь до вашего файла с данными(в формате .csv)")
    print("Для выхода из программы напишите 'exit'")
    user_csv = input()
    if user_csv.lower() == 'exit':
        menu_exit = False
        break
    if user_csv.endswith('csv') is False:
        print('Путь неправильный')
    else:
        user_csv.replace("\\", "/")
        user_csv = str(Path(user_csv))
        print('1 - Вывести топ-10 участков дороги по кол-ву аварий')
        print('2 - Вывести графический вид по всем участкам дороги')
        main_choice = input('Введите пункт меню ')
        if int(main_choice) == 2:
            build_graph(into_dict(import_csv_data(user_csv)))
        elif int(main_choice) == 1:
            top = into_dict_top10(import_csv_data(user_csv))
            for i in range(10):
                print(top[i])
        else:
            print('Неправильный пункт меню')

        print("Хотите продолжить работу? (пишите 'yes' или 'no')")
        answer = input()
        if answer.lower() == 'no':
            menu_exit = False