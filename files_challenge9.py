#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 14 Jan 2024
# Date Modified : -
# Description   :  
# Usage         : files_challenge9.py
#####   #####   #####

"""
Write a Python script that reads the file in a dictionary. 
The words in the file will be the dictionary keys 
and the length of each word the corresponding values.
"""

if __name__ == '__main__':
    with open('american-english.txt', 'r') as f:
        content = f.read().splitlines()
    
    file_dict = {}
    for element in content:
        file_dict[element] = len(element)
    
    print(file_dict)