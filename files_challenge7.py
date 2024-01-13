#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 13 Jan 2024
# Date Modified : -
# Description   : bank account counter
# Usage         : files_challenge7.py
#####   #####   #####

"""
Write a Python program that calculates the net amount of a bank account based on the transactions that are saved in a text file.
The file format is as follows:

D:50
W:100

D means deposit while W means withdrawal.

Suppose that the following file is supplied to the program:

D:300
D:300
W:500
D:200

Then, the output should be: 300
"""

def bank_account_counter(file_name):
    deposit = []
    withdraw = []
    with open(file_name, 'r') as f:
        content = f.read().split()
        # print(content)
        for number in content:
            if number[0] == 'D':
                deposit.append(int(number[2:]))
            else:
                withdraw.append(int(number[2:]))
    # print(deposit)
    # print(withdraw)
    return f'Total = {sum(deposit) - sum(withdraw)}'

if __name__ == '__main__':
    print(bank_account_counter('banking.txt'))
