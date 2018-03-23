import argparse
from os import listdir
from os.path import isfile, join, getsize


def parse_input_parameters():
    parser = argparse.ArgumentParser(description="Exports all objects to folder in export script directory")
    parser.add_argument("source", metavar='source_directory', type=str, help="Path to source directory")
    parser.add_argument("target", metavar='target_directory', type=str, help="Path to target directory")
    return parser.parse_args()


def find_appropriate_files(directory, prefix, max_size):
    total_size = 0
    number_of_files = 0
    for file in listdir(directory):
        full_filename = join(directory, file)
        size = getsize(full_filename)
        if isfile(full_filename) and file.startswith(prefix) and (size <= max_size):
            total_size += size
            number_of_files += 1
    return total_size, number_of_files


args = parse_input_parameters()
if args.source == args.target:
    print("ERROR. Source and target directories coincide.")
    exit(1)
prefix = input("Filename start char sequence: ")
max_size_in_bytes = int(input("Maximum size of file in bytes: "))
total_size, number_of_files = find_appropriate_files(args.source, prefix, max_size_in_bytes)
print("Files transferred:\t", number_of_files)
print("Bytes transferred:\t", total_size)

