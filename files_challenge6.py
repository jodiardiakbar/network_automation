#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 13 Jan 2024
# Date Modified : -
# Description   : linux wc like application
# Usage         : files_challenge6.py
#####   #####   #####

"""
Write a Python program to count the number of lines, 
words, and characters in a text file. 
This is similar to the Linux `wc` command. 
Create a function, if possible.
"""

def linux_wc(file_name):
    with open(file_name, 'r') as f:
        content_lines = f.readlines()
        lines = len(content_lines)
    
    with open(file_name, 'r') as f:
        content_words = f.read().split()
        words = len(content_words)
    
    with open(file_name, 'r') as f:
        content_characters = f.read()
        word_count = 0
        for character in content_characters:
            word_count += 1

    return f'{file_name} contain of {lines} lines, {words} words, and {word_count} characters'

if __name__ == '__main__':
    print(linux_wc('sample_file.txt'))
