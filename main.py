import argparse
import os

######### FUNCTIONS #########

"""Read a file"""
def read_file(file):
    with open(file, 'r') as f:
        f_content = f.read()
        print(f_content, end='')

"""Write a file"""
def write_file(file):
    with open(file, 'w+') as f:
        print("{} file created.".format(file))

"""Append a file"""
def append_content(file):
    file_content = input("Enter content: ")
    with open(file, 'a+') as f:
        f.write("\n{}".format(file_content))
        print("{} is updated.".format(file))

"""Append a file"""
def concat_file(file):
    file_to_concat = input("Enter file to be appended to: ")
    fin = open(file, "r")
    concat_result = fin.read()
    fout = open(file_to_concat, "a")
    fout.write(concat_result)
    print("Concat succes!")

"""Delete a file"""
def delete_file(file):
    os.remove(file)
    print("{} file deleted.".format(file))

def main():
    """Argument Parser"""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-w", "--write", help="Create new file.", action="store_true")
    group.add_argument("-a", "--append", help="Append a file.", action="store_true")
    group.add_argument("-r", "--read", help="Read a file.", action="store_true")
    group.add_argument("-c", "--concat", help="Concat files.", action="store_true")
    group.add_argument("-d", "--delete", help="Delete a file.", action="store_true")
    parser.add_argument("file", help="Read a file.", type=str)

    args = parser.parse_args()
    print("------ {} ------".format(args.file))

    """Function arguments"""
    if args.write:
         write_file(args.file)
    elif args.append:
        append_content(args.file)
    elif args.read:
        read_file(args.file)
    elif args.concat:
        concat_file(args.file)
    elif args.delete:
        delete_file(args.file)
    else:
        print("Error.")

if __name__ == "__main__": 
    main()
