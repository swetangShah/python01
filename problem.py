import os

directory_path = '/'  # Remove the accidental space before 'directory_path'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

for item in contents:
    print(item)  # Correct indentation
