#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 5 Jan 2024
# Date Modified : -
# Description   : from file to a list to a string and print
# Usage         : files_challenge2.py
#####   #####   #####

"""
Create a Python script that reads a text file into a list 
and then converts the list into a string that has the entire file content.
"""

if __name__ == '__main__':
    with open('sample_file.txt', 'r') as f:
        content_as_list = f.read().split()
        print(content_as_list)
        print('#' * 50)
        # content_as_string = ''.join(content_as_list)
        # print(content_as_string)

        for i in content_as_list:
            print(i)
