import shutil
from pathlib import Path

# -----------------------------
# Base paths (IDE-friendly)
# -----------------------------
BASE_DIR = Path.cwd()              # current working directory
SOURCE_DIR = BASE_DIR / "Test"
DEST_DIR = BASE_DIR / "backup"

FILE_1 = BASE_DIR / "test1.txt"
FILE_2 = BASE_DIR / "test2.txt"
FILE_3 = BASE_DIR / "test3.txt"

PROJECT_DIR = BASE_DIR / "project_shutil"
BACKUP_DIR = BASE_DIR / "project_shutil_backup"


# -----------------------------
# File operations
# -----------------------------

# Move file or folder
# shutil.move(SOURCE_DIR, DEST_DIR)

# Copy file (content only)
# shutil.copy(FILE_1, FILE_2)

# Copy file (content + metadata)
# shutil.copy2(FILE_1, FILE_3)


# -----------------------------
# Directory operations
# -----------------------------

# Copy entire directory
# shutil.copytree(PROJECT_DIR, BACKUP_DIR)

# Delete directory permanently (USE WITH CAUTION)
# shutil.rmtree(BACKUP_DIR)


# -----------------------------
# Archive operations
# -----------------------------

# Create ZIP archive
# shutil.make_archive("project_shutil", "zip", PROJECT_DIR)
