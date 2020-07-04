#!/usr/bin/env python3

FILE = './xmp/nums'

def main():
    with open (FILE) as all_lines:
        sum_of_values = 0.
        for line in all_lines:
            sum_of_values += float(line)
            print(f'value: {line} & sum: {sum_of_values}')


if __name__ == '__main__':
    main()
    exit()
