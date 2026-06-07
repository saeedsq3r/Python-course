import sys

# Python version
print(sys.version)

# Platform (Windows/Linux/Mac)
print(sys.platform)

# Python search paths
print(sys.path)

# Command line arguments
print(sys.argv)

# Python executable path
print(sys.executable)

# Size of object in bytes
print(sys.getsizeof(10))

# Recursion limit
print(sys.getrecursionlimit())

# Set recursion limit
sys.setrecursionlimit(2000)

# Maximum integer size
print(sys.maxsize)

# Loaded modules
print(sys.modules)

# Standard output stream
print(sys.stdout)

# Error output stream
print(sys.stderr)

# Write to console
sys.stdout.write("Hello\n")

# Write error message
sys.stderr.write("Error\n")

# Built-in modules list
print(sys.builtin_module_names)

# Python version details
print(sys.version_info)