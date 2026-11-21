# PRINTS the contents of directory using module
import os
# use the directory path where you want to list the contents
path = "D:\\phyton"
# use the os.listdir() method to get the list of files and directories in the specified path
contents = os.listdir(path)
print("Contents of the directory:")
for item in contents:
    print(item)