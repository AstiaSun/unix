import argparse


def parse_input_parameters():
    parser = argparse.ArgumentParser(description="Exports all objects to folder in export script directory")
    parser.add_argument("folder", metavar='path_to_directory', type=str, help="Folder where to place exported objects")
    parser.add_argument("prefix", metavar='filename_prefix', type=str, help="Char sequence from which file's name begins")
    return parser.parse_args()


def find_appropriate_files(directory, prefix):
    import os
    result = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            if str(name).startswith(prefix):
                result.append(path)
    return result


def write_result(filename, found_directories):
    output = open(filename, "w")
    for dir in found_directories:
        output.write(dir + "\n")
    output.close()


args = parse_input_parameters()
found_directories = find_appropriate_files(args.folder, args.prefix)
filename = input("Filename: ")
write_result(filename, found_directories)



