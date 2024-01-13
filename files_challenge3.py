#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 5 Jan 2024
# Date Modified : -
# Description   : remove all empty lines including spaces
# Usage         : files_challenge3.py
#####   #####   #####

"""
Create a Python script that removes all empty lines 
including those that contain only spaces from a file.
"""

if __name__ == '__main__':
    with open('file.txt', 'r') as f:
        content = f.read().split()
        print(content)
    
    with open('filenew.txt', 'a') as f:
        for line in content:
            f.write(f'{line}\n')

    print('#' * 50)

    with open('filenew.txt', 'r') as f:
        print(f.read())
