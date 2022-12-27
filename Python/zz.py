import os

# Specify the directories containing the Python files
directories = 'Python/python_Basic_problems', 'Python/Python'

# Initialize an empty list to store the file names and paths
files = []

# Iterate over the list of directories
for directory in directories:
  # Use os.walk() to recursively search for Python files in the current directory
  for root, _, filenames in os.walk(directory):
    for filename in filenames:
      # Add the file name and path to the list of files if it is a Python file
      if filename.endswith('.py'):
        files.append((filename, os.path.join(root, filename)))

# Open the main file for writing
with open('main.py', 'w') as main_file:
  # Write a header for the main file
  main_file.write('# This file was generated by combining multiple Python files\n')
  
  # Iterate over the list of file names and paths
  for file_name, file_path in files:
    # Open the current file for reading
    with open(file_path, 'r') as f:
      # Write a comment indicating the name of the current file to the main file
      main_file.write('\n# File: {}\n'.format(file_name))
      # Write the contents of the current file to the main file
      main_file.write(f.read())

print('Combined Python files in specified directories into main.py')