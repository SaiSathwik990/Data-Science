'''
program to read and write binary data
'''
import os

source_file = input("Please enter source filename/path to read binary data : ")
dest_file = input("Please enter destination filename/path to write binary data : ")

if os.path.exists(source_file):
    #file reading
    with open(source_file, "rb") as file:
        data = file.read()
    file.close()

    #file writing
    with open(dest_file, "wb") as file:
        file.write(data)
    file.close()
    print()
    print("Binary data successfully written to "+dest_file)
else:
    print("Either source of destination file path does not exists")
    
    
