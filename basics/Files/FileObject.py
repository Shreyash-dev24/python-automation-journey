"""
FILE HANDLING IN PYTHON
----------------------
This file demonstrates:
1. Reading text files
2. File pointer control (tell, seek)
3. Reading large files efficiently
4. Writing to files
5. Copying text files
6. Copying binary files (images) safely using chunks

Recommended approach:
Always use context managers (with statement).
"""


# =========================================================
# 1. OPENING AND READING A FILE (TEXT MODE)
# =========================================================

# Using context manager so file closes automatically
with open('read.txt', 'r') as f:
    
    # Number of characters to read at a time
    size_to_read = 10
    
    # Read first 10 characters
    f_contents = f.read(size_to_read)
    print(f_contents)

    # Show current position of file pointer
    print(f.tell())

    # Read next 10 characters
    f_contents = f.read(size_to_read)
    print(f_contents)


# =========================================================
# 2. READING A FILE LINE BY LINE (BEST FOR LARGE FILES)
# =========================================================

with open('read.txt', 'r') as f:
    for line in f:
        print(line, end='')   # end='' avoids extra new lines


# =========================================================
# 3. READLINE AND READLINES
# =========================================================

with open('read.txt', 'r') as f:
    
    # Reads one line at a time
    line1 = f.readline()
    line2 = f.readline()
    
    print(line1)
    print(line2)

    # Reads all lines and returns a list
    all_lines = f.readlines()
    print(all_lines)


# =========================================================
# 4. WRITING TO A FILE
# =========================================================

# 'w' mode creates file if not exists
# 'w' mode OVERWRITES existing content
with open('write.txt', 'w') as f:
    f.write("Writing in a file using write mode.\n")
    f.write("Previous content will be erased.\n")


# =========================================================
# 5. COPYING TEXT FROM ONE FILE TO ANOTHER
# =========================================================

with open('read.txt', 'r') as rf:
    with open('copy_paste.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# =========================================================
# 6. COPYING BINARY FILES (IMAGES, VIDEOS, PDF)
# =========================================================
# IMPORTANT:
# - Use 'rb' for reading binary
# - Use 'wb' for writing binary
# - Text mode will CORRUPT binary files
# =========================================================


# ---------------------------------------------------------
# 6.1 SIMPLE BINARY COPY
# ---------------------------------------------------------

with open('xp_img.jpeg', 'rb') as rf:
    with open('copy_img.jpeg', 'wb') as wf:
        for chunk in rf:
            wf.write(chunk)


# ---------------------------------------------------------
# 6.2 BINARY COPY USING CHUNKS (BEST PRACTICE)
# ---------------------------------------------------------
# This is memory efficient and works for very large files
# ---------------------------------------------------------

with open('xp_img.jpeg', 'rb') as rf:
    with open('copy_img_while.jpeg', 'wb') as wf:
        
        chunk_size = 4096   # 4 KB per read
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


# ========================================================
# END OF FILE
# ========================================================
