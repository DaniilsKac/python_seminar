def enter_first_name():
    return input("Введите имя абонента: ").title()


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_address_number():
    return input("Введите адрес абонента: ").title()

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def search_line():
    print("Выберите вариант поиска:\n"
          "1. Имя\n"
          "2. Фамилия\n"
          "3. Отчество\n"
          "4. Телефон\n"
          "5. Адрес")
    index = int(input("Введите вариант: ")) - 1
    searched = input("Введите поисковые данные: ").title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[item]:
                print(item, end='\n\n')
        # file.seek(0)
        # print(file.readlines())

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def interface():
    cmd = 0
    while cmd != '6':
        print("Выберите действие:\n"
            "1. Добаваить контакт\n"
            "2. Вывести все контакты\n"
            "3. Поиск контакта\n"
            "4. Редактирование контакта\n"
            "5. Удалить контакт\n"
            "6. Выход\n")
        cmd = input("Выберите действие: ")
        while cmd not in('1', '2', '3', '4', '5', '6'):
            print("Некорректный ввод")
            cmd = input("Введите действие: ")
        match cmd:
            case '1': 
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                edit_file()
            case '5':
                delete_info()
            case '6':
                print("Всего доброго!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def edit_file():
    print("Выберите элемент для поиска контакта:\n"
          "1. Имя\n"
          "2. Фамилия\n"
          "3. Отчество\n"
          "4. Телефон\n"
          "5. Адрес")
    
    index = int(input("Элемент для поиска: ")) - 1
    searched = input("Введите данные для редактирования: ").title()
    replacement = input("Введите новые данные: ").title()

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')

    new_data = []

    for item in data:
        contact_info = item.replace('\n',' ').split()
        if len(contact_info) >= index + 1:
            if contact_info[index] == searched:
                contact_info[index] = replacement
                new_data.append(f'{contact_info[0]} {contact_info[1]} {contact_info[2]} {contact_info[3]} {contact_info[4]}\n')
            else:
                new_data.append(item)
        else:
            new_data.append(item)

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_data))

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_info():
    print("Выберите что удалить:\n"
          "1. Удалить всю информацию контакта\n"
          "2. Имя\n"
          "3. Фамилия\n"
          "4. Телефон\n"
          "5. Адрес\n")
    index = int(input("Введите вариант: ")) - 1
    searched = input("Введите поисковые данные: ").title()

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')

    new_data = []

    for item in data:
        if index == 5 and searched in item:
            continue
        contact_info = item.replace('\n',' ').split()

        if len(contact_info) >= index + 1:
            info_to_delete = contact_info[index]
            if searched == info_to_delete and index != 5:
                contact_info[index] = 'deleted'
                new_data.append(f'{contact_info[0]} {contact_info[1]} {contact_info[2]} {contact_info[3]} {contact_info[4]}\n')
            else:
                new_data.append(item)
        else:
            new_data.append(item)

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_data))

#--------------------------------------------------------------------------------------------------------------------------------------------------------

interface()