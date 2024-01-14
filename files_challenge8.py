#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 14 Jan 2024
# Date Modified : -
# Description   : lines differ checker
# Usage         : files_challenge8.py
#####   #####   #####

"""
Write a Python script that compares line by line two text files
and displays the lines that differ.
"""

from collections import Counter

def line_differ_checker(file_name1, file_name2):
    with open(file_name1, 'r') as f:
        content1 = f.read().splitlines()
        # print(f'content1: {content1}')

    with open(file_name2, 'r') as f:
        content2 = f.read().splitlines()
        # print(f'content2: {content2}')

    content = content1 + content2
    content_dict = Counter(content)
    result = [k for k,v in content_dict.items() if v == 1]
    return result
    
if __name__ == '__main__':
    print(line_differ_checker('file1.txt', 'file2.txt'))
    