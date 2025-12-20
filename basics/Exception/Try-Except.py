"""
PYTHON EXCEPTION HANDLING + ERROR LOGGING (PRACTICAL)
====================================================

This script demonstrates:
- try / except / else / finally
- Proper error logging using logging module
- Difference between handling vs recording errors

This is INTERN-READY and REAL-WORLD SAFE.
"""

import logging

# -------------------------------------------------
# LOGGER CONFIGURATION
# -------------------------------------------------
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
)

try:
    # -------------------------------------------------
    # TRY BLOCK
    # -------------------------------------------------
    F = open('tex.txt')   # may raise FileNotFoundError

    # Intentional error for demonstration
    if F.name == 'text.txt':
        raise Exception("Manual exception raised for testing")

except FileNotFoundError as e:
    # -------------------------------------------------
    # SPECIFIC EXCEPTION
    # -------------------------------------------------
    logging.error("File not found", exc_info=True)
    print("File does not exist.")

except Exception as e:
    # -------------------------------------------------
    # GENERIC EXCEPTION
    # -------------------------------------------------
    logging.error("Unexpected error occurred", exc_info=True)
    print("Error!!")

else:
    # -------------------------------------------------
    # ELSE BLOCK
    # -------------------------------------------------
    print(F.read())
    F.close()

finally:
    # -------------------------------------------------
    # FINALLY BLOCK
    # -------------------------------------------------
    print("Execution Finally.....")
