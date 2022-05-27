import xml.etree.ElementTree as ET
from collections import defaultdict, Counter
from copy import deepcopy
from datetime import datetime
from random import randrange
from timeit import timeit
import inspect

from requests import get, utils


def easy_timeit(func, params, iters=1000):
    def retrieve_name(var):
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]

    func_str = f"{func.__name__}({retrieve_name(params)[0]})"
    setup_str = f"{retrieve_name(params)[0]} = {params}"
    print('Time required for {} iterations: {} сек'.format(iters, timeit(func_str, number=iters, globals=globals(),
                                                                         setup=setup_str)))


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

    for value in zip(l1, l2):
        _tmp[value[0]].append(value[1])
    return dict(_tmp)


def thesaurus_adv(*args: str):
    l1 = [value.partition(' ')[2][0] for value in args]  # Первая буква фамилии
    l3 = list(args)
    _tmp = defaultdict(list)
    for _key, value in zip(l1, l3):
        _tmp[_key[0]].append(value)
    for key in _tmp.keys():
        _l1 = [value.partition(' ')[0] for value in _tmp[key]]
        _tmp2 = defaultdict(list)
        for _key2, value2 in zip(_l1, _tmp[key]):
            _tmp2[_key2[0]].append(value2)
        _tmp[key] = dict(_tmp2)
    return dict(_tmp)


def thesaurus_adv_sorted(*args):
    l1 = sorted([value.partition(' ')[2][0] for value in args])  # Первая буква фамилии
    l3 = sorted(list(args))
    _tmp = defaultdict(list)
    for _key, value in zip(l1, l3):
        _tmp[_key[0]].append(value)
    for key in _tmp.keys():
        _l1 = [value.partition(' ')[0] for value in _tmp[key]]
        _tmp2 = defaultdict(list)
        for _key2, value2 in zip(_l1, _tmp[key]):
            _tmp2[_key2[0]].append(value2)
        _tmp[key] = dict(_tmp2)
    return dict(_tmp)


def get_jokes(jokes_num, repeat=0):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    _tmplist = []
    for n in range(jokes_num):
        if not repeat:
            _tmplist.append(
                [nouns.pop(randrange(len(nouns))), adverbs.pop(randrange(len(adverbs))),
                 adjectives.pop(randrange(len(adjectives)))])
        else:
            _tmplist.append(
                [nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))],
                 adjectives[randrange(len(adjectives))]])
    for idx, item in enumerate(_tmplist):
        _tmplist[idx] = ' '.join(item)
    return _tmplist


def currency_check(*cur_code: str):
    currency_response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    site_encoding = utils.get_encoding_from_headers(currency_response.headers)
    content_decoded = currency_response.content.decode(encoding=site_encoding)
    myroot = ET.fromstring(content_decoded)

    cur_date = datetime.strptime(myroot.attrib['Date'], "%d.%m.%Y")
    _returnlist = {'Date': cur_date.strftime("%d-%m-%Y")}
    for code in cur_code:
        for x in myroot.findall('Valute'):
            if x.find('CharCode').text == code:
                _returnlist.update({x.find('Name').text: x.find("Value").text})

    return _returnlist


def odd_nums(max_value):
    for value in range(max_value + 1):
        if value % 2 != 0:
            yield value


def odd_nums_noyield(max_value):
    return (value for value in range(max_value + 1) if value % 2 != 0)


def cort_task(tutors: list, klasses: list):
    for x in range(len(tutors) - len(klasses)):
        klasses.append(None)
    return ((tutor, klass) for tutor, klass in zip(tutors, klasses))


def next_more_previous(src: list):
    list_gen = (item for item in src)
    _tmp = []
    _a = src[0]
    for _b in list_gen:
        if _a < _b:
            _tmp.append(_b)
        _a = _b

    return _tmp


def no_intersect(src: list):
    temp_list = deepcopy(src)
    list_gen = (item for item in temp_list)
    _tmp = []
    for _b in list_gen:
        src.remove(_b)
        if _b not in src:
            _tmp.append(_b)
        src.append(_b)

    return _tmp


def no_intersect_2(src: list):
    return [item for item, count in Counter(src).items() if count == 1]
