"""
OS MODULE – BASIC OPERATIONS
Author: Shreyash
Purpose: Demonstrate commonly used functions from the os module
"""

import os
from datetime import datetime

# --------------------------------------------------
# 1. CURRENT WORKING DIRECTORY
# --------------------------------------------------

# Returns the current working directory
print("Current Working Directory:", os.getcwd())

# Change the current working directory
# (Use relative paths for GitHub safety)
# os.chdir("some_directory")

# --------------------------------------------------
# 2. DIRECTORY LISTING
# --------------------------------------------------

# Lists files and folders in the current directory
# print("Directory Contents:", os.listdir())

# --------------------------------------------------
# 3. DIRECTORY CREATION
# --------------------------------------------------

# Create a single directory
# os.mkdir("Demo_Folder")

# Create nested directories (parent + child)
# os.makedirs("Demo_Folder/Sub_Folder")

# --------------------------------------------------
# 4. DIRECTORY DELETION
# --------------------------------------------------

# Remove an empty directory
# os.rmdir("Demo_Folder")

# Remove nested empty directories
# os.removedirs("Demo_Folder/Sub_Folder")

# --------------------------------------------------
# 5. FILE / DIRECTORY RENAMING
# --------------------------------------------------

# Rename a file or directory
# os.rename("old_name.py", "new_name.py")

# --------------------------------------------------
# 6. FILE METADATA (STATISTICS)
# --------------------------------------------------

# Returns information about a file
# file_stats = os.stat("example.txt")

# File creation time (platform dependent)
# mod_time = file_stats.st_ctime
# print("File Creation Time:", datetime.fromtimestamp(mod_time))

# --------------------------------------------------
# 7. DIRECTORY TREE TRAVERSAL
# --------------------------------------------------

# Walk through directory tree
# for dirpath, dirnames, filenames in os.walk("."):
#     print("Current Path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filenames)
#     print()

# --------------------------------------------------
# 8. ENVIRONMENT VARIABLES
# --------------------------------------------------

# Fetch environment variable value
# print("User Environment Variable:", os.environ.get("USER"))

# --------------------------------------------------
# 9. PATH OPERATIONS (os.path)
# --------------------------------------------------

sample_path = "example/test.txt"

# Split path into directory and file
print("Split Path:", os.path.split(sample_path))

# Check if path exists
print("Path Exists:", os.path.exists(sample_path))

# Check if path is a directory
print("Is Directory:", os.path.isdir(sample_path))

# Check if path is a file
print("Is File:", os.path.isfile(sample_path))

# Split filename and extension
print("Split Extension:", os.path.splitext(sample_path))










