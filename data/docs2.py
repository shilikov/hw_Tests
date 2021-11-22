help = ('''
p –  команда, по номеру локумента выведет имя человека, которому он принадлежит;
s –  команда, по номеру документа покажет номер полки, на которой он находится;
l –  команда, выведет список всех документов;
a –  команда, которая добавит новый документ в каталог и в перечень полок;
d –  команда, удалит документ из каталога и из перечня полок;
m –  команда переместит документ с текущей полки на целевую.
s –  команда, которая спросит номер новой полки и добавит ее в перечень.;'
q -  команда для завершения программы
''')


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def helper():
    return help

def people(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def owners(autor_lest):
    owner = [doc_number for doc_number in documents if doc_number['number'] == autor_lest]
    return owner[0]["name"] if owner else f'документ не найден'



def shelves(shelves_namber):
        shelvers = [shelves_list for shelves_list, item in directories.items() if shelves_namber in item]
        return f'документ #{shelves_namber} расположен на полке: - #{shelvers[0]}' if shelvers \
            else f'документ не найден на полке'




def documentc_list():
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))


def documents_add(doc_type, doc_number, doc_names, direct_num):
    # if direct_num in directories:
    if direct_num in directories.keys():
        # documents.append({'type': doc_type, 'number': doc_number, 'name': doc_names})
        documents.append(dict(type=doc_type, number=doc_number, name=doc_names))
        # directories[direct_num].append(doc_number)
        return direct_num if direct_num else f"такой полки нет"


def doc_del(del_doc):
    for document in range(len(documents)):
        if documents[document]['number'] == del_doc:
            del documents[document]
            for direct in directories.values():
                if del_doc in direct:
                    direct.remove(del_doc)
                    print('документ удален')
                    doc = True
                    return del_doc, doc
        else:
            print(f'Ошибка неудаетъся добавить документ проверте корректность введеных данных!')
            break



def mov_dirrect(number_dir, autor_dir):
    for direct_val in directories.values():
        if number_dir in direct_val:
            direct_val.remove(number_dir)
            directories[autor_dir].append(number_dir)
            print('Документ перемещен: -')
    else:
        print('запрашиваемый документ не найден')


def selv_add(add_selvers):
    if add_selvers in directories.keys():
        print('папка уже существует')
    else:
        if add_selvers not in directories.keys():
            directories_list = {add_selvers: []}
            directories.update(directories_list)
            return add_selvers, True
        print("\n  Полка добавлена.")
        return add_selvers, False



def archive():
    print('\nКаталог документов.')
    for document in documents:
        print('  {0} "{1}" "{2}"'.format(document['type'], document['number'], document['name']))

    print('\nПеречень полок, на которых находятся документы.')
    for num_shelf, doc_num in directories.items():
        print('  Полка №', num_shelf, doc_num)





# def pasword(qwerty):
#     if qwerty == (400103273):
#         print('OK')
#     else:
#         print("gfhjkmyt dtysq")
#         exit()

# for i in range(3):
#             user_int = int(input('----'))
#             if user_int == (400103273):
#                 print('OK')
#             else:
#             # if i == 2:
#             print("gfhjkmyt dtysq")
#         my_quit()
#         emaill()


# for i in range(3):
#  print("Введите пароль:")
#  s = input()
#  if s == "Omega":
#   print("Доступ открыт.")
#   break
#  else: print("Неверный пароль, попробуйте снова.")
#  if i == 2: print("Доступ запрещён")

# def emaill():
#     email = input("enter email  ")
#     if '@' in email:
#         print()
#     else:
#         print('адрес указан неверно проверьте')
#         return emaill()


def program():
    print(f'╔┓┏╦━━╦┓╔┓╔━━╗'"\n"
          f'║┗┛║┗━╣┃║┃║╯╰║'"\n"
          f'║┏┓║┏━╣┗╣┗╣╰╯║'"\n"
          f'╚┛┗╩━━╩━╩━╩━━╝')
    print('Я менджер документов!')
    print(f'████▀▀▀▀▀▀████▀▀███'"\n"
          f'███░▄░▄░╖░▐████▄░▐█'"\n"
          f'█░▄░░░┬░║▒▐████▀░▐█'"\n"
          f'█▄┴───┘░╙─┘▒▒▒▒░▄██'"\n"
          f'████▌░░░░░░░░░░░███'"\n"
          f'█████▒██░███▒██░███'"\n"
          f'████▄▄█▄▄██▄▄█▄▄███')

    # user_int = int(input('----'))
    # if user_int == (400103273):
    #     print('OK')
    # else:
    #     print("gfhjkmyt dtysq")
    #     exit()
    # emaill()

    while True:

        print("Для просмотра доступных комманд ведите: - h ")
        user_input = input('введите команду - ')
        if user_input == 'p':
            people(input("введите номер документа - "))
        elif user_input == 's':
            shelves(input('введите номер документа - '))
        elif user_input == 'l':
            documentc_list()
        elif user_input == 'a':
            documents_add(input('\nВведите тип документа:- '),
                          input('Введите номер документа: '), input('Введите имя: '),
                          input('Введите номер полки (1, 2, 3): '))
            print(archive())
        elif user_input == 'd':
            doc_del(input("веедите номер документа который нужно удалить "))
            print(archive())
        elif user_input == "sa":
            selv_add(input("Введите номер папки "))
            print(archive())
        elif user_input == "m":
            mov_dirrect(input("введите номер докумнета: - "),
                        input("номер папки в которую хотите переместить: - "))
        elif user_input == 'h':
            print(helper())
        if user_input == 'q':
            print('проограмма завершена')
            print(f'╭ ╯╭╯╭╯'"\n"
                  f'███████ ═╮'"\n"
                  f'█☆★☆★█ ▏ ▏'"\n"
                  f'███████ ═╯'"\n"
                  f'◥█████◤')
            break

if __name__ == "__main__":
    program()
