import xml.etree.ElementTree as ET
from collections import defaultdict, Counter
from copy import deepcopy
from datetime import datetime
from random import randrange
from timeit import timeit
import inspect
import os
from os import stat, curdir
import time
import csv
import itertools
from re import compile
import shutil
from copy import copy

# Imports for suppressing print statements
import contextlib, sys
from io import StringIO

from requests import get, utils


# context manager for no print
@contextlib.contextmanager
def nostdout(print_once=False):
    """

    Prevent print to stdout, but if there was an error then catch it and
    print the output before raising the error.
    """

    saved_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield
    except Exception:
        saved_output = sys.stdout
        sys.stdout = saved_stdout
        print(saved_output.getvalue())
        raise
    saved_output = sys.stdout
    sys.stdout = saved_stdout
    if print_once:
        print(saved_output.getvalue())


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


def simple_timeit(func, retries=1, suppress_print=False, print_once=False) -> None:
    """
    Takes function to time it execution

    :param func: function to time
    :param retries: number of retries
    :param suppress_print: suppresses prints to stdout of func
    :param print_once: print func's print once even if print is suppressed
    :return: None
    """
    start_time = time.monotonic_ns()
    retries -= int(print_once)
    for _ in range(retries):
        if suppress_print:
            with nostdout():
                func()
        elif print_once and not suppress_print:
            with nostdout():
                func()
        else:
            func()

    if print_once:
        with nostdout(print_once):
            func()

    print("--- Execution took {} ms, number of retries: {} ---".format((time.monotonic_ns() - start_time) / 1_000_000,
                                                                       retries + int(print_once)))


def odd_nums(max_value):
    for value in range(max_value + 1):
        if value % 2 != 0:
            yield value


def odd_nums_noyield(max_value):
    return (value for value in range(max_value + 1) if value % 2 != 0)


def cort_task(tutors: list, klasses: list):
    [klasses.append(None) for _ in range(len(tutors) - len(klasses))]
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


def github_example_parse(filename, url):
    from re import compile
    message_format = compile(
        r'(?P<IP>(?:\d{1,3}\.){3}\d{1,3}).*?(?P<datetime>\[.*?\]).*?"(?P<oper>\w+) (?P<address>.*?)"(?P<other>.+)')
    try:
        with open(filename, 'x') as f:
            file_res = get(url)
            site_encoding = utils.get_encoding_from_headers(file_res.headers)
            content_decoded = file_res.content.decode(encoding=site_encoding)
            f.write(content_decoded)
    except FileExistsError:
        if stat(curdir + '/' + filename).st_size == 0:
            with open(filename, 'w') as f:
                file_res = get(url)
                site_encoding = utils.get_encoding_from_headers(file_res.headers)
                content_decoded = file_res.content.decode(encoding=site_encoding)
                f.write(content_decoded)
    with open(filename, 'r') as f:
        newline = (item for item in f)
        try:
            for line in newline:
                match = message_format.match(line)
                parsed_ip = match.group('IP')
                parsed_oper = match.group('oper')
                parsed_addr = match.group(('address'))
                yield parsed_ip, parsed_oper, parsed_addr
        except AttributeError:
            message_format_bad = compile(
                r'(?P<IP>.*?) -.*?(?P<datetime>\[.*?\]).*?"(?P<oper>\w+) (?P<address>.*?)"(?P<other>.+)')
            match = message_format_bad.match(line)
            parsed_ip = match.group('IP')
            parsed_oper = match.group('oper')
            parsed_addr = match.group(('address'))
            yield f'Not usual IP: {parsed_ip}', parsed_oper, parsed_addr


def csv_files_write(filename):
    #
    # with open('hobbies.csv', 'w', newline='') as f:
    #     # lines = [
    #     #     'Иванов,Иван,Иванович',
    #     #     'Петров,Петр,Петрович'
    #     # ]
    #     lines = [
    #         'скалолазание,охота',
    #         'горные лыжи'
    #     ]
    #     print(lines)
    #     csv_file_writer = csv.writer(f, dialect='excel', delimiter='\n', quoting=csv.QUOTE_NONE)
    #     csv_file_writer.writerow(lines)

    with open(filename, 'w', newline='') as write_file:
        csv_file_writer = csv.writer(write_file, dialect='excel', delimiter=':', quoting=csv.QUOTE_NONE)
        with open('names.csv', 'r') as f:
            with open('hobbies.csv', 'r') as f2:
                csv_reader_1 = csv.reader(f, dialect='excel', delimiter='\n')
                csv_reader_2 = csv.reader(f2, dialect='excel', delimiter='\n')
                final_dict = {}

                for (key, value) in itertools.zip_longest(csv_reader_1, csv_reader_2, fillvalue='None'):
                    if key not in ['None', '']:
                        if value == ['']:
                            value = 'None'
                        final_dict.update({''.join(key): ''.join(value)})
                    else:
                        return 1

        csv_file_writer.writerows(final_dict.items())
    return f'Wrote to file {filename}'


def csv_files_write_nodict(filename):
    #
    # with open('hobbies.csv', 'w', newline='') as f:
    #     # lines = [
    #     #     'Иванов,Иван,Иванович',
    #     #     'Петров,Петр,Петрович'
    #     # ]
    #     lines = [
    #         'скалолазание,охота',
    #         'горные лыжи'
    #     ]
    #     print(lines)
    #     csv_file_writer = csv.writer(f, dialect='excel', delimiter='\n', quoting=csv.QUOTE_NONE)
    #     csv_file_writer.writerow(lines)

    with open(filename, 'w') as write_file:
        with open('names.csv', 'r') as f:
            with open('hobbies.csv', 'r') as f2:
                csv_reader_1 = csv.reader(f, dialect='excel', delimiter='\n')
                csv_reader_2 = csv.reader(f2, dialect='excel', delimiter='\n')

                for (key, value) in itertools.zip_longest(csv_reader_1, csv_reader_2, fillvalue='None'):
                    if key not in ['None', '']:
                        if value == ['']:
                            value = 'None'
                        # final_dict.update({''.join(key): ''.join(value)})
                        write_file.write(f"{''.join(key)}: {''.join(value)}\n")
                    else:
                        return 1

    return f'Wrote to file {filename}'


def build_structure(filename) -> None:
    last_pathlen = 0
    last_name = ''
    root = os.path.abspath(os.path.curdir)
    print(root)
    start_len_pattern = r'(?P<level>[\s\|\-]+)(?P<name>[^\.]+)(?P<extention>\.{1,}[^\.]+)?'
    pattern_match = compile(start_len_pattern)
    with open(filename, 'r') as f:
        for line in f:
            match = pattern_match.match(line)

            start = match.group('level')
            name = match.group('name').strip()
            try:
                extension = match.group('extention').strip()
            except AttributeError:
                extension = None

            if extension is None:
                if last_pathlen > len(start):
                    for _ in range(int((last_pathlen - len(start)) / 2)):
                        os.chdir('..')
                if len(start) > last_pathlen:
                    try:
                        os.chdir(last_name)
                    except OSError:
                        pass
                try:
                    os.mkdir(name)
                except FileExistsError:
                    print(f'Dir {name} already exists')
            else:
                if len(start) > last_pathlen:
                    os.chdir(last_name)
                if last_pathlen > len(start):
                    for _ in range(int((last_pathlen - len(start)) / 2)):
                        os.chdir('..')
                try:
                    with open(f'{name}{extension}', 'x'):
                        pass
                except FileExistsError:
                    print(f'File {name}{extension} already exists')
            last_pathlen = len(start)
            last_name = name


def gather_templates() -> None:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    # try:
    #     os.mkdir('my_project/global_templates')
    # except FileExistsError:
    #     pass
    for root, dirs, files in os.walk(os.path.join(ROOT_DIR, 'my_project')):
        for dir in dirs:
            if dir == 'templates':
                print(shutil.copytree(os.path.join(root, dir), os.path.join(ROOT_DIR, 'my_project\global_templates'),
                                      dirs_exist_ok=True))
