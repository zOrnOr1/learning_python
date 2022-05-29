import argparse
import sys


def main(argv):
    program, *args = argv
    parser = argparse.ArgumentParser()
    parser.add_argument('--n1', '-n1', help="Names .csv file", type=str, required=1)
    parser.add_argument('--n2', '-n2', help="Hobbies .csv file", type=str, required=1)
    parser.add_argument('--o', '-o', help="Output .csv file", type=str, default='nodict_file.txt')


    args = parser.parse_args()
    with open(args.o, 'w') as write_file:
        with open(args.n1, 'r') as f:
            with open(args.n2, 'r') as f2:
                csv_reader_1 = csv.reader(f, dialect='excel', delimiter='\n')
                csv_reader_2 = csv.reader(f2, dialect='excel', delimiter='\n')

                for (key, value) in itertools.zip_longest(csv_reader_1, csv_reader_2, fillvalue='None'):
                    if key not in ['None', '']:
                        if value == ['']:
                            value = 'None'
                        # final_dict.update({''.join(key): ''.join(value)})
                        write_file.write(f"{''.join(key)}: {''.join(value)}\n")
                    else:
                        print('Exit code 1')
                        return 1

    print(f'Wrote to file {args.o}')


if __name__ == '__main__':
    import csv
    import itertools

    exit(main(sys.argv))
