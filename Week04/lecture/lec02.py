import os

file_name = "file.txt"

if os.path.exists(file_name):
    print("File existed")
else:
    print("File not existed")