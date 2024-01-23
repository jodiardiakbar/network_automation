#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 16 Jan 2024
# Date Modified : -
# Description   :  
# Usage         : files_challenge11.py
#####   #####   #####

"""
Consider this dictionary file.
Write a Python script that finds the number
of occurrences of each letter of the alphabet in all the words
of the dictionary. 
Make a distinction between lower and uppercase letters.
You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' 
and so on appear in all the words in the dictionary.
Which is the most frequently used letter in English words? 
But the least frequently used one?
"""

if __name__ == '__main__':
    with open('american-english.txt', 'r') as f:
        content = f.read()
        # print(content)
    
    letter_counter = {}
    for letter in content:
        if letter == '\n':
            continue
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    
    print(letter_counter)

    print('#' * 50)
    top_g = sorted(letter_counter.items(), key=lambda x: x[1], reverse=True)
    print(top_g)

    print('#' * 50)
    low_g = sorted(letter_counter.items(), key=lambda x: x[1])
    print(low_g)