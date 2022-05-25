### GeekBrains lesson 2 + GitHub test ###
from string import punctuation


def lesson_decorator(func):
    def wrapper(*args: str):
        print('\n')
        print('=' * 30)
        print(f"Lesson {args[0]}")
        func(*args)

    return wrapper


def part_decorator(func):
    def wrapper(*args: str):
        func(f"Part {args[1]}")
        print('=' * 30)

    return wrapper


@lesson_decorator
@part_decorator
def part_print(*args: str):
    """
    :param args: lesson, part
    :return: None
    """
    print(args[0])


def duration_print(*args):
    for num in args:
        print(f'Asserted number: {num}')
        if num < 60:
            print(f'Result: {num} сек')
        if 3600 > num >= 60:
            print(f'Result: {num // 60} мин {num % 60} сек')
        if 86400 > num >= 3600:
            print(f'Result: {num // 3600} ч {num % 3600 // 60} мин {num % 3600 % 60} сек')
        if num >= 86400:
            print(f'Result: {num // 86400} дн {num % 86400 // 3600} ч {num % 3600 // 60} мин {num % 3600 % 60} сек')


def find_sum(list_of_nums: list):
    """
    :param list_of_nums:
    :return: total_sum
    """
    total_sum = 0
    for item in list_of_nums:
        sum_num = 0
        _temp = item
        while item:
            sum_num += item % 10
            item //= 10
        total_sum += _temp if sum_num % 7 == 0 else 0

    return total_sum


def my_dict_test(phrase: str):
    if int(phrase) in range(10, 20):
        phrase = phrase[len(phrase) - 2:]
    else:
        phrase = phrase[len(phrase) - 1:]
    phrase_dict = {
        "0": "процентов",
        "1": "процент",
        "2": "процента",
        "3": "процента",
        "4": "процента",
        "11": "процентов",
        "12": "процентов",
        "13": "процентов",
        "14": "процентов"
    }
    phrase_dict.setdefault(phrase, 'процентов')
    return phrase_dict[phrase]


def lesson_1():
    # Part 1
    part_print(1, 1)
    duration_print(53, 153, 4153, 400153, 123141341241)

    # Part 2
    part_print(1, 2)
    cube_list = [num ** 3 for num in range(1, 1000, 2)]
    print(f'Сгенерированный лист: {cube_list}')
    print(f'List id = {id(cube_list)}')
    # Task a
    print('\nTask a:')
    print(f'Сумма равна: {find_sum(cube_list)}')
    # Task b
    print('\nTask b + c:')
    for idx, num in enumerate(cube_list):
        cube_list[idx] = num + 17
    print(f'List id = {id(cube_list)}')
    print(f'Сумма равна: {find_sum(cube_list)}')

    # Part 3
    part_print(1, 3)

    for val in range(21):
        print(f"{str(val)} {my_dict_test(str(val))}")


def lesson_2():
    # Part 1
    part_print(2, 1)
    print(f"Type of 15 * 3: {type(15 * 3)}")
    print(f"Type of 15 / 3: {type(15 / 3)}")
    print(f"Type of 15 // 2: {type(15 // 2)}")
    print(f"Type of 15 ** 2: {type(15 ** 2)}")

    # Part 2
    part_print(2, 2)
    given_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

    idx = 0
    for item in range(len(given_list)):
        if given_list[idx][0] not in punctuation:
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


if __name__ == "__main__":
    lesson_1()
