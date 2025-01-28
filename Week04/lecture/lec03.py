import os

file_name = "file.txt"

if os.path.exists(file_name):
    with open(file_name, "r") as textfile: #text file is an alias for file_name
        content = textfile.read()
        print(content)

else:
    print("File not existed")

# open()