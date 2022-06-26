import csv
import re

with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)


def permutation_of_initials(list_of_lists):
    """Перестановка ФИО в правильные ячейки"""
    for item in list_of_lists:

        if len(item[1].split()) == 2:
            item[2] = item[1].split()[1]
            item[1] = item[1].split()[0]

        if len(item[0].split()) == 3:
            item[2] = item[0].split()[2]
            item[1] = item[0].split()[1]
            item[0] = item[0].split()[0]

        if len(item[0].split()) == 2:
            item[1] = item[0].split()[1]
            item[0] = item[0].split()[0]

    return list_of_lists


def new_list_creator(old_contacts_list):
    """Создание нового списка контактов без дублирования"""
    new_contacts_list = []
    list_of_lastnames_and_firtsnames = []
    old_contacts_list = permutation_of_initials(old_contacts_list)

    for item in old_contacts_list:
        tuple_of_lastname_and_firtsname = (item[0], item[1])
        if tuple_of_lastname_and_firtsname not in list_of_lastnames_and_firtsnames:
            list_of_lastnames_and_firtsnames.append(tuple_of_lastname_and_firtsname)
            new_contacts_list.append(item)

        for elem in new_contacts_list:
            if item[0] == elem[0] and item[1] == elem[1]:
                for i in range(len(elem)):
                    if elem[i] == '':
                        elem[i] = item[i]

    return new_contacts_list


def application_of_a_single_format_of_numbers_in_the_list(some_list):
    """Форматирование номеров телефона по заданному шаблону"""
    some_list = new_list_creator(some_list)
    pattern = r'(\+7|8)?\s*\(?(\d{3})\)?\s*-*(\d{3})(-|\s)?(\d{2})(-|\s)?(\d{2})\s*\(?(доб.)?\s*(\d{4})?'
    substitution = r'+7(\2)\3-\5-\7 \8\9'
    for item in some_list:
        res = re.sub(pattern, substitution, item[5])
        item[5] = res

    return some_list


if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(application_of_a_single_format_of_numbers_in_the_list(contacts_list))
