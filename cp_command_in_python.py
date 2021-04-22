"""
Cp command implementation in python

"""
from sys import argv
import os


def open_src_file(src):

    with open(src, 'r') as f:
        lines = f.read()
        return lines




 #   copy file function


def copy(src, dest):

    try:
        filedata = open_src_file(src)

        with open(dest, 'w') as fd:
            fd.write(filedata)

    except FileNotFoundError:
        print(" FileNotFoundError Ocurred ")


   # Main function

def main():

    if len(argv) != 3:
        print('Run this Script Like this -> python3.6 copy.py <src_file_path> <destination_file_path>')
        return
    _, src, dest =  argv


    if not os.path.isfile(src):
        print(f'No such file or directory: {src} ')
        return

    if src == dest:
        print(f'{src} and {dest} are same files')
        return

   # call to copy function

    copy(src, dest)


if __name__ == '__main__':
    main()
