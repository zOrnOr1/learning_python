### GeekBrains lesson 2 + GitHub test ###
from string import punctuation


def lesson_2():
    # Part 1
    print(f"Type of 15 * 3: {type(15 * 3)}")
    print(f"Type of 15 / 3: {type(15 / 3)}")
    print(f"Type of 15 // 2: {type(15 // 2)}")
    print(f"Type of 15 ** 2: {type(15 ** 2)}")

    print("==========================================")
    # Part 2
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
    lesson_2()
