#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 25 Jan 2024
# Date Modified : -
# Description   :  
# Usage         : files_challenge12.py
#####   #####   #####

"""
Change the solution from the previous challenge 
so that the script considers all letters lowercase 
(it makes no distinction between lower and uppercase letters).
"""

if __name__ == '__main__':
    with open('american-english.txt', 'r') as f:
        content = f.read()
        # print(content)
    
    letter_counter = {}
    for letter in content:
        if letter.lower() == '\n':
            continue
        if letter.lower() in letter_counter:
            letter_counter[letter.lower()] += 1
        else:
            letter_counter[letter.lower()] = 1
    
    print(letter_counter)

    print('#' * 50)
    top_g = sorted(letter_counter.items(), key=lambda x: x[1], reverse=True)
    print(top_g)

    print('#' * 50)
    low_g = sorted(letter_counter.items(), key=lambda x: x[1])
    print(low_g)