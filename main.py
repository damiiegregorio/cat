#file objects
import os

def isReadFile(choose_file):
    with open(choose_file, 'r') as f:
        f_content = f.read()
        print(f_content, end='')

def isWriteFile(choose_file):
    with open(choose_file, 'w') as f:
        pass

def isWriteContent(choose_file):
    file_content = input("Enter content: ")
    with open(choose_file, 'a+') as f:
        f.write(file_content)

def isDeleteFile(choose_file):
    os.remove(choose_file)
    print("{} file deleted.".format(choose_file))

print("Read a file    --- 1")
print("Add a file     --- 2")
print("Add content    --- 3")
print("Delete content --- 4")
choice = input("Enter your choice: ")
choose_file = input("Filename: ")

if choice == "1":
    ans = isReadFile(choose_file)
elif choice == "2":
    ans = isWriteFile(choose_file)
    print("{} file created.".format(choose_file))
elif choice == "3":
    ans = isWriteContent(choose_file)
elif choice == "4":
    ans = isDeleteFile(choose_file)
else:
    print("Error")
