def main(argv):
    program, *args = argv
    result = sum(map(int, args))
    print(f'Результат: {result}')

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
