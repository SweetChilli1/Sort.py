#!/usr/bin/env python3


import os
import shutil
from argparse import ArgumentParser

def make_dir(file, directory, mode):                                  # creates folders either by name or type of file, and moves the files to the correct folders
    try:
        new_dir = os.path.join(directory, mode[1:] if mode[0] == '.' else mode)
        os.makedirs(new_dir, exist_ok=True)
        file_to_move  = os.path.join(new_dir, file)
        shutil.move(file, file_to_move)
    except Exception as e:
        print(f'ERROR: When moving from: {file}: {e}')

def select_mode(file, directory, mode ):                              # select the mode
    try: 
        name, typ = os.path.splitext(file)
    except NameError:
        pass
    if mode:
        make_dir(file, directory, name )
    else:
        make_dir(file, directory, typ) 


def read_files(files, directory, mode):                               # reads the files in the directory
    for file in files:
        if os.path.isfile(file):
            select_mode(file, directory, mode)      
        else:
            pass


def main():

    parser = ArgumentParser(description='Sorts the files from a directory into different folders.')
    parser.add_argument( '-n', '--name', action='store_true', help='Sorts the files by name.')
    parser.add_argument( '-d', '--directory', help='Sorted specified directory')
    
    args = parser.parse_args()

    current_directory = os.getcwd()

    if args.directory:                                     # checks if the parameter '--directory' was used
        directory = os.listdir(args.directory)
    else:
        directory = current_directory
    
    files = os.listdir(directory)

    if args.name:                                           # checks if the parameter '--name' was used
        read_files(files, directory, True)
    else:
        read_files(files, directory, False)    
    


if __name__ == '__main__':
    main()