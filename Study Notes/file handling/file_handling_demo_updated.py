"""
FILE HANDLING

1. Open the file (use open function - need the filename and the file permission)
2. Do the operations (read, write, append)
3. Close the file

File permissions:
    r - read permission, read-only access, if file does not exists it will raise an error
    w - write permission, write access but OVERWRITES the entire contents of the file
      - if file does not exits, it will create a new file
    a - append permission, write access but only add line/s at the end of the last line
      - if file does not exits, it will create a new file
"""
# absolute path - starts from root dir e.g., C:\Users\jsarcillo\PyCharmProjects\pythonProject
# relative path - starts with respect to current directory
import os
curr_dir = os.getcwd()
print(curr_dir)             # to know the current directory where we execute the script

# give us the full path of the file we want to open
file_path = os.path.abspath('sample_file.txt')

# the not good practice approach is to open the file and manually close the file handle
print("The bad practice")
myfile = open(file_path, 'r')     # myfile is a file object where you can access file's contents

for line in myfile:               # iterate through each line in the file
    name = line.strip()           # need to remove the newline character at the end of each line
    print(name)
myfile.close()      # programmers forget this most of the time, hence a bad practice

# best practice approach is to use 'with' context manager to take care of closing resources
print("The good practice")
with open(file_path, 'r') as myfile:
    new_contents = []
    for line in myfile:
        name = line.strip()
        print(name)

# opening file with write access - be CAREFUL on this because it overwrites the contents of the file
with open(file_path, 'w') as myfile:
    myfile.write("BINI COLET")
    # now check the sample_file.txt, BINI COLET took over solo

# creating a new file
with open("sample_file2.txt", 'w') as myfile:
    myfile.write("This is a new file.")
    # now check the sample_file2.txt created in the current directory

# appending new lines in a file
with open(file_path, 'a') as myfile:
    myfile.write("\n")              # to make sure we won't appending at the end of the current last line
    myfile.write("BINI MIKHA\n")
    myfile.write("BINI MALOI\n")
    myfile.write("BINI JHOANNA\n")
    myfile.write("BINI GWEN\n")
    myfile.write("BINI AIAH\n")
    myfile.write("BINI SHEENA\n")
    myfile.write("BINI STACEY\n")

    showtimers = ['BINI VICE', 'BINI VHONG', 'BINI ANNE']
    eb_hosts = ['BINI JOSE', 'BINI WALLY', 'BINI MAINE  ']

    # or we can add in bulk
    new_members = "\n".join(showtimers)
    myfile.write(new_members)
    myfile.write("\n")
    new_members = "\n".join(eb_hosts)
    myfile.write(new_members)

    # now check the changes in sample_file.txt
    # welcome back ladies and welcome to the new members!


# what if we want to replace a specific line? e.g. replace BINI WALLY with BINI VIC
# the 'r+' attribute allows you to read the contents of the file
# and perform append write operations but not overwriting it.
with open(file_path, 'r+') as myfile:
    names = []                          # let's temporarily store each line in a list
    for line in myfile:
        name = line.strip()
        if name == "BINI WALLY":        # we want to replace the line containing "BINI WALLY"
            names.append("BINI VIC")
        else:
            names.append(name)
    new_contents = "\n".join(names)

    myfile.seek(0)                      # resets the file pointer at the beginning of the file
    myfile.write(new_contents)          # write the updated contents to the file
