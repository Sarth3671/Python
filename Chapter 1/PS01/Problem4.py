import os

''''Write a python program to print the contents of a directory using the os module. 
Search online for the function which does that.'''
 
# Specify the directory path
path = '/'

# List all entries in the specified directory
entries = os.listdir(path)

# Print the entries
for entry in entries:
    print(entry)
