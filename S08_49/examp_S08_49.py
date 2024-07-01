# Для установки библиотеки вывода данных в виде таблицы
# pip install prettytable

from prettytable import PrettyTable

def work_with_phonebook():

    choice=show_menu()

    phone_book=read_txt('phon.txt')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            find_item=input('Фамилия ')
            # print(find_by_lastname(phone_book,last_name))
            find_by(phone_book,find_item,'Фамилия')
        elif choice==3:
            # number=input('number ')
            # print(find_by_number(phone_book,number))
            find_item=input('Телефон ')
            find_by(phone_book,find_item,'Телефон')
        elif choice==4:
            lastname=input('Фамилия ')
            delete_by_lastname(phone_book,lastname)
            write_txt('phon.txt',phone_book)
        elif choice==5:
            last_name=input('Фамилия ')
            new_number=input('Новый номер ')
            change_number(phone_book,last_name,new_number)
            print_result(phone_book)
            write_txt('phon.txt',phone_book)
        elif choice==6:
            print('Укажите через запятую следующие данные нового абонента:')
            print('фамилия,имя,номер телефона,описание')
            print('Например:')
            print('Иванов,Иван,111,описание Иванова')
            user_data=input('новый абонент: ')
            add_user(phone_book,user_data)
            print_result(phone_book)
            write_txt('phon.txt',phone_book)

        choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Удалить абонента по фамилии\n"
          "5. Изменить номер абонента по фамилии\n"
          "6. Добавить абонента в справочник\n"
		  "7. Закончить работу\n")
    choice = int(input('Введите номер действия: '))
    return choice


# Иванов,Иван,111,описание Иванова
# Петров,Петр,222,описание Петрова
# Васичкина,Василиса,333,описание Васичкиной
# Питонов,Антон,777,умеет в Питон
# Питонов,Антон,777,умеет в Питон

def read_txt(filename): 

    phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	

    return phone_book

def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}')
            # phout.write(f'{s[:-1]}\n')

def print_result(phb):
    if len(phb) == 0:
        print('Данные отсутствуют')
    else:
        # Создаем объект PrettyTable
        table = PrettyTable()

        # Добавляем заголовки столбцов
        lbls = phb[0]
        table.field_names = lbls.keys()

        # Добавляем строки данных
        for i in phb:
            try:
                table.add_row(i.values())
            except ValueError:
                pass
    
        # Выводим таблицу
        print(table)

def find_by(phone_book,find_item,find_key):
    find_list = []
    for i in phone_book:
        if find_item in (i[find_key]):
            find_list.append(i)
    print_result(find_list)

def delete_by_lastname(phone_book,lastname):

    del_data = []
    del_index = []

    for i in range(len(phone_book)):
        del_d = phone_book[i]
        if lastname in (del_d['Фамилия']):
            del_data.append(del_d)
            del_index.append(i)

    for i in range(len(del_index), 0, -1):
        del phone_book[del_index[i-1]]
    print('Удалены абоненты:')
    print_result(del_data)
    

def add_user(phone_book,user_data):
    # phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)	
    return phone_book


def change_number(phone_book,last_name,new_number):
    for i in range(len(phone_book)):
        phb = phone_book[i]
        if phb['Фамилия'] == last_name:
            phb['Телефон'] = new_number
    return phone_book


work_with_phonebook()