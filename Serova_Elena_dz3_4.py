#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
#возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
#содержащие имена, начинающиеся с соответствующей буквы. Например:
# thesaurus("Иван", "Мария", "Петр", "Илья")
#{"И": ["Иван", "Илья"],
#"М": ["Мария"],
#"П": ["Петр"]}
#Написать функцию thesaurus_adv(), принимающую в качестве аргументов
#строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
#фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
#записи, в которых фамилия начинается с соответствующей буквы


def thesaurus_adv(*args):
    key_surname = sorted(set(x.split(' ')[1][0] for x in args))
    dictionary = {}
    for surname in key_surname:
        dictionary[surname] = list(filter(lambda x: x.split(' ')[1][0] == surname, args))
        key_name = sorted(set(x[0] for x in dictionary[surname]))
        name_dictionary = {}
        for name in key_name:
            name_dictionary[name] = list(filter(lambda x: x[0] == name, dictionary[surname]))
        dictionary[surname] = name_dictionary
    return dictionary

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
