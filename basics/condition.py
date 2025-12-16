"""
COMPLETE PYTHON CONDITIONALS
============================
This file covers ALL conditional constructs and patterns in Python:

1. if / elif / else
2. Comparison operators
3. Logical operators (and, or, not)
4. Identity vs Equality (is vs ==)
5. Membership operators (in, not in)
6. Truthy and Falsy values
7. Nested conditionals
8. Conditional (ternary) expressions
9. pass statement
10. None checking (best practice)
11. Short-circuit evaluation
12. match-case (Python 3.10+)
13. Common mistakes and best practices

This file is IDE-ready and interview-safe.
"""

# -------------------------------------------------
# 1. BASIC if / elif / else
# -------------------------------------------------
language = "Python"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("Unknown language")


# -------------------------------------------------
# 2. COMPARISON OPERATORS
# >, <, >=, <=, ==, !=
# -------------------------------------------------
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# -------------------------------------------------
# 3. LOGICAL OPERATORS
# and, or, not
# -------------------------------------------------
user = "Admin"
logged_in = True
banned = False

if user == "Admin" and logged_in and not banned:
    print("Access granted")
else:
    print("Access denied")


# -------------------------------------------------
# 4. IDENTITY vs EQUALITY
# is  -> identity (memory)
# ==  -> value equality
# -------------------------------------------------
x = None

if x is None:
    print("x is None (correct usage)")

# ❌ BAD PRACTICE (do not do this)
# if x == None:

a = 10
b = 10

if a == b:
    print("Values are equal")

# 'is' should NOT be used for numbers or strings
# if a is b:   # ❌ unreliable


# -------------------------------------------------
# 5. MEMBERSHIP OPERATORS
# in, not in
# -------------------------------------------------
languages = ["Python", "Java", "C"]

if "Python" in languages:
    print("Python found")

if "Go" not in languages:
    print("Go not found")


# -------------------------------------------------
# 6. TRUTHY AND FALSY VALUES (CRITICAL)
# Falsy values:
# False, None, 0, 0.0, "", [], {}, set()
# -------------------------------------------------
data = []

if data:
    print("Data exists")
else:
    print("Data is empty")

name = ""

if not name:
    print("Name is missing")


# -------------------------------------------------
# 7. NESTED if STATEMENTS
# -------------------------------------------------
marks = 85

if marks >= 40:
    if marks >= 75:
        print("Distinction")
    else:
        print("Passed")
else:
    print("Failed")


# -------------------------------------------------
# 8. CONDITIONAL (TERNARY) EXPRESSION
# -------------------------------------------------
status = "Logged in" if logged_in else "Logged out"
print(status)


# -------------------------------------------------
# 9. pass STATEMENT
# Used as a placeholder
# -------------------------------------------------
condition = True

if condition:
    pass  # logic to be added later
else:
    print("Condition false")


# -------------------------------------------------
# 10. SHORT-CIRCUIT EVALUATION
# -------------------------------------------------
# Second condition executes ONLY if first is True
x = 0

if x != 0 and (10 / x) > 1:
    print("Won't reach here")
else:
    print("Safe due to short-circuiting")


# -------------------------------------------------
# 11. MULTIPLE CONDITIONS WITH PRECEDENCE
# -------------------------------------------------
a, b, c = 5, 10, 0

if (a < b and b > c) or c == 0:
    print("Condition satisfied")


# -------------------------------------------------
# 12. match-case (Python 3.10+)
# Modern alternative to if-elif ladder
# -------------------------------------------------
command = "start"

match command:
    case "start":
        print("System starting")
    case "stop":
        print("System stopping")
    case "restart":
        print("System restarting")
    case _:
        print("Unknown command")


# -------------------------------------------------
# 13. COMMON INTERVIEW MISTAKES (DOCUMENTED)
# -------------------------------------------------

# ❌ Wrong
# if logged_in == True:

# ✔ Correct
if logged_in:
    print("Logged in (clean check)")

# ❌ Wrong
# if value is 5:

# ✔ Correct
value = 5
if value == 5:
    print("Value is 5")
