#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 5 Jan 2024
# Date Modified : -
# Description   : duplicate mac address remover
# Usage         : files_challenge1.py
#####   #####   #####

"""
Consider this text file that contains multiple duplicate MAC addresses.
Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.
"""

if __name__ == '__main__':
    with open('macs.txt', 'r') as f:
        all_macs = f.read().split()
        unique_macs = list(set(all_macs))
    print(unique_macs)

    with open('macs_new.txt', 'a') as f:
        for mac in unique_macs:
            f.write(f'{mac}\n')
    
    print('#' * 50)

    with open('macs_new.txt', 'r') as f:
        content = f.read()
        print(content)
            
