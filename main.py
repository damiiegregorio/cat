#file objects

def isReadFile(choose_file):
    with open(choose_file, 'r') as f:
        f_content = f.read()
        print(f_content, end='')

def isWriteFile(choose_file):
    with open(choose_file, 'w') as f:
        pass

print("Read a file  --- 1")
print("Write a file --- 2")
choice = input("Enter your choice: ")
choose_file = input("Filename: ")

if choice == "1":
    ans = isReadFile(choose_file)
elif choice == "2":
    ans = isWriteFile(choose_file)
    print("{} file created.".format(choose_file))
    file_content = input("Input conte")
else:
    print("Error")