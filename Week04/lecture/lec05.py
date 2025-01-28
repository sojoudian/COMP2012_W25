import os

file_name = "file.txt"

if os.path.exists(file_name):
    with open(file_name, "r") as textfile: #text file is an alias for file_name
        content = textfile.read()
        if content.strip():
            print("File content:")
            print(content)
        else:
            print("The file is empty!")    

else:
    print("File not exist. Creating a new file")
    student_name = "Maziar Sojoudian"
    student_id = 500223344
    with open(file_name, "w") as textFile:
        textFile.write(f"Name: {student_name}\n")
        textFile.write(f"ID: {student_id}\n")
    # Read and Display the created file
    with open(file_name, "r") as textFile:
        print("Added file content:")    
        print(textFile.read())