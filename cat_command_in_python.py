from sys import argv
import os


def read_file(fname):

    try:
        with open(fname,"r") as fd:
            for line in fd:
                yield line
    except:
        print('some error occurred')

  # Main function

def main():

    if len(argv) != 2:
        print('Usage of Script  ->  python3.6 cat.py <file_path> ')
        return

    _, fname = argv

    if not os.path.isfile(fname):
        print(f'No such file: {fname} ')
        return

    for line in read_file(fname):
        print(line)


if __name__ == '__main__':
    main()