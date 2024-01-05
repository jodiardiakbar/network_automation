#!./venv/bin/python

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