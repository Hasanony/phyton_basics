# PRINTS the contents of directory using module
import os
path = "D:\\phyton"
contents = os.listdir(path)
print("Contents of the directory:")
for item in contents:
    print(item)