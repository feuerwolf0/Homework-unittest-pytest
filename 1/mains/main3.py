#Домашнее задание к лекции 4.Коллекции данных.Словари.Множества» Задание 2

def main(ids): 
    uniq_ids = []
    for item in ids.values():
        uniq_ids += item
    # print('Уникальные гео-ids:', list(set(uniq_ids)))
    return f'Уникальные гео-ids: {list(set(uniq_ids))}'

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids2 = {'user1': [88, 22, 19, 75, 75],
       'user2': [89, 24, 24, 100, 100],
       'user3': [54, 98, 98, 35]}

if __name__ == '__main__':
    print(main(ids2))