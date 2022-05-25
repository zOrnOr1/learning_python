from collections import defaultdict


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


def num_translate(number_to_translate: str):
    trans_dict = {
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
    return trans_dict.get(number_to_translate, None)


def num_translate_adv(number_to_translate: str):
    trans_dict = {
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
    if number_to_translate.istitle():
        result = trans_dict.get(number_to_translate.lower(), None).title()
    else:
        result = trans_dict.get(number_to_translate, None)

    return result


def thesaurus(*args):
    l1 = [value[0] for value in args]
    l2 = [value for value in args]
    _tmp = defaultdict(list)
    # _tmp = dict(zip(l1, l2))
    # _tmp = dict.fromkeys(key[0] for key in args)
    for value in zip(l1, l2):
        _tmp[value[0]].append(value[1])
    return dict(_tmp)


def thesaurus_adv(*args: str):
    l1 = [value.partition(' ')[2][0] for value in args]  # Первая буква фамилии
    # l2 = [value.partition(' ')[0][0] for value in args]  # Первая буква имени
    l3 = [value for value in args]
    _tmp = defaultdict(list)

    for value in zip(l1, l3):
        if value[1].partition(' ')[2][0] == value[0]:
            _tmp[value[0]].append(value[1])
    print(dict(_tmp))
    for key in _tmp.keys():
        for text in _tmp[key]:
            _l1 = [item for item in text]
        print(_l1)

        _l2 = [text for text in _tmp[key]]

        # _tmp[key].append()

    # for name in args:
    #     if name.partition(' ')[2][0] not in _tmp:
    #         _tmp[name.partition(' ')[2][0]].append()
