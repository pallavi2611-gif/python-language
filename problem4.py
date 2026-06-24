from importlib.resources import path
import os

# select the directory whose contents you want to list 
directory_path = '/'

contents = os.listdir(directory_path)

# print the contents of the directory)
print(contents)