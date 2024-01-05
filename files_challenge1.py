#!./venv/bin/python

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
            