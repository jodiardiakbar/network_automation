#!./venv/bin/python

if __name__ == '__main__':
    with open('sample_file.txt', 'r') as f:
        content_as_list = f.read().split()
        print(content_as_list)
        print('#' * 50)
        # content_as_string = ''.join(content_as_list)
        # print(content_as_string)

        for i in content_as_list:
            print(i)