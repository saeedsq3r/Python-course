import os

# Name of operating system
print(os.name)

# Current working directory
print(os.getcwd())

# List files in directory
print(os.listdir())

# Create a new folder
os.mkdir("test_folder")

# Remove folder
os.rmdir("test_folder")

# Check if file exists
print(os.path.exists("demo.txt"))

# Absolute path of file
print(os.path.abspath("demo.txt"))

# Get file name from path
print(os.path.basename("folder/file.txt"))

# Get directory name from path
print(os.path.dirname("/home/user/file.txt"))

# Rename file
os.rename("old.txt", "new.txt")

# Delete file
os.remove("file.txt")

# Environment variables
print(os.environ)

# Get logged-in user
print(os.getlogin())

# CPU count
print(os.cpu_count())

# Run system command
print(os.system("echo Hello"))

# File size
print(os.path.getsize("demo.txt"))

# Check directory
print(os.path.isdir("test"))

# Check file
print(os.path.isfile("demo.txt"))

# Change directory
os.chdir("..")

# Walk directory tree
print(os.walk("."))