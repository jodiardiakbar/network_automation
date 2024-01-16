#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 16 Jan 2024
# Date Modified : -
# Description   :  
# Usage         : files_challenge10.py
#####   #####   #####

"""
Consider the dictionary file from the previous challenge.
Write a Python script that finds the first 100 longest words
in the file.
"""

if __name__ == '__main__':
    with open('american-english.txt', 'r') as f:
        content = f.read().splitlines()
    
    file_dict = {}
    for element in content:
        file_dict[element] = len(element)
    
    top_longest_words = sorted(file_dict.items(), key=lambda x: x[1], reverse=True)
    print(f'top 100 longest words: {top_longest_words[:100]}')