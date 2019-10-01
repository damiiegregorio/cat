#file objects

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

print("Read a file    --- 1")
print("Add a file     --- 2")
print("Add content    --- 3")
choice = input("Enter your choice: ")
choose_file = input("Filename: ")

if choice == "1":
    ans = isReadFile(choose_file)
elif choice == "2":
    ans = isWriteFile(choose_file)
    print("{} file created.".format(choose_file))
elif choice == "3":
    ans = isWriteContent(choose_file)
else:
    print("Error")
