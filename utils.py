import csv
from errors import InstantiateCSVError
import matplotlib.pyplot as plt


def import_csv_data(csv_data):
    """ Функ-ция принимает csv файл с данными и преобразует в оформленный список словарей, c участком дороги
    и количеством аварий соответственно"""
    try:
        with open(csv_data, encoding='utf-8') as r_file:
            bad_roads = []
            road_section_id = 0
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter=",")
            # Считывание данных из CSV файла
            for row in file_reader:
                need_key = False
                if len(bad_roads) == 0:
                    for i in range(len(row)):
                        if row[i] == 'УчастокДороги':
                            road_section_id = i
                # проверка, если первая строчка с шапкой названий или неверно заполненные данные
                if row[road_section_id].isdigit():
                    if len(bad_roads) != 0:
                        for i in bad_roads:
                            for k, v in i.items():
                                if k == row[road_section_id]:
                                    i[k] += 1
                                    need_key = True

                    if (len(bad_roads) == 0) or (need_key is False):
                        data = {f'{row[road_section_id]}': 1}
                        bad_roads.append(data)

                else:
                    continue
            return bad_roads
    except FileNotFoundError:
        print("По указанному пути файл отсутствует")

    except InstantiateCSVError:
        print("Файл поврежден")


def into_dict(data):
    "Фун-я первода данных в нужный нам словарь"
    clear_dict = {}
    for i in data:
        for k, v in i.items():
            clear_dict[k] = v
    sorted_clear_dict = sorted(clear_dict.items(), key=lambda item: item[0])

    return sorted_clear_dict


def into_dict_top10(data):
    "Фун-я первода данных в нужный нам словарь"
    clear_dict = {}
    for i in data:
        for k, v in i.items():
            clear_dict[k] = v
    sorted_clear_dict = sorted(clear_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_clear_dict


def build_graph(data):
    'посторим график по данным'
    X = []
    Y = []

    for i in data:
        X.append(i[0])
        Y.append(i[1])

    plt.plot(X, Y)
    plt.xlabel('Участок дороги')
    plt.ylabel('Кол-во аварий')
    plt.show()