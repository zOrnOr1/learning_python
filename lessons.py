### GeekBrains lesson 2 + GitHub test ###
import func_lib as lib
from timeit import timeit


def lesson_1():
    # Part 1
    lib.part_print(1, 1)
    lib.duration_print(53, 153, 4153, 400153, 123141341241)

    # Part 2
    lib.part_print(1, 2)
    cube_list = [num ** 3 for num in range(1, 1000, 2)]
    print(f'Сгенерированный лист: {cube_list}')
    print(f'List id = {id(cube_list)}')
    # Task a
    print('\nTask a:')
    print(f'Сумма равна: {lib.find_sum(cube_list)}')
    # Task b
    print('\nTask b + c:')
    for idx, num in enumerate(cube_list):
        cube_list[idx] = num + 17
    print(f'List id = {id(cube_list)}')
    print(f'Сумма равна: {lib.find_sum(cube_list)}')

    # Part 3
    lib.part_print(1, 3)

    for val in range(21):
        print(f"{str(val)} {lib.my_dict_test(str(val))}")


def lesson_2():
    # Part 1
    lib.part_print(2, 1)
    print(f"Type of 15 * 3: {type(15 * 3)}")
    print(f"Type of 15 / 3: {type(15 / 3)}")
    print(f"Type of 15 // 2: {type(15 // 2)}")
    print(f"Type of 15 ** 2: {type(15 ** 2)}")

    # Part 2
    lib.part_print(2, 2)
    given_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

    idx = 0
    for item in range(len(given_list)):
        if given_list[idx][0] not in lib.punctuation:
            if given_list[idx].isdigit():
                given_list[idx] = f"{int(given_list[idx]):02d}"
                given_list.insert(idx, '"')
                idx += 1
                given_list.insert(idx + 1, '"')
                idx += 1
        else:
            if given_list[idx][1:].isdigit():
                given_list[idx] = f"{given_list[idx][0]}{int(given_list[idx][1:]):02d}"
                given_list.insert(idx, '"')
                idx += 1
                given_list.insert(idx + 1, '"')
                idx += 1
        idx += 1

    given_list = ' '.join(given_list)
    for idx in range(len(given_list)):
        try:
            if given_list[idx] == '"':
                if given_list[idx - 3].isdigit():
                    given_list = f'{given_list[:idx - 1]}{given_list[idx:]}'
                if given_list[idx + 3].isdigit():
                    given_list = f'{given_list[:idx + 1]}{given_list[idx + 2:]}'
        except IndexError:
            pass
    print(given_list)


def lesson_3():
    # Part 1
    lib.part_print(3, 1)
    trans_dict_for_test = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    for key in trans_dict_for_test.keys():
        print(lib.num_translate(key))
    print(f"При невозможности перевода: {lib.num_translate('key')}")

    # Part 2
    lib.part_print(3, 2)
    print(f"Asserted: One, Result: {lib.num_translate_adv('One')}")
    print(f"Asserted: one, Result: {lib.num_translate_adv('one')}")

    # Part 3
    lib.part_print(3, 3)
    print(timeit('lib.thesaurus("Иван", "Мария", "Петр", "Илья")', number=1000, globals=globals()))
    print(lib.thesaurus("Иван", "Мария", "Петр", "Илья"))

    # Part 4
    lib.part_print(3, 4)
    print(timeit('lib.thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")',
                 number=1000, globals=globals()))
    print(lib.thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))


if __name__ == "__main__":
    lesson_1()
