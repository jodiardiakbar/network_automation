#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 5 Jan 2024
# Date Modified : -
# Description   : tail function to read n lines from a file
# Usage         : files_challenge4.py
#####   #####   #####


def tail(file_name, n):
    with open(file_name, 'r') as f:
        content = f.read().splitlines()
        starting_line = len(content) - n
        for line in content[starting_line:]:
            print(line)


if __name__ == '__main__':
    tail('sample_file.txt', 5)