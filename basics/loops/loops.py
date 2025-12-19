"""
COMPLETE PYTHON LOOPS
====================
This file covers ALL looping constructs and patterns in Python:

1. for loop
2. while loop
3. range()
4. break, continue, pass
5. for-else and while-else
6. Nested loops
7. Looping over:
   - list
   - tuple
   - set
   - dictionary
   - string
8. enumerate()
9. zip()
10. Infinite loops
11. Loop control with conditions
12. Common mistakes and best practices

IDE-ready. Interview-safe. Practical.
"""

# -------------------------------------------------
# 1. BASIC for LOOP
# -------------------------------------------------
languages = ["Python", "Java", "C"]

for lang in languages:
    print(lang)


# -------------------------------------------------
# 2. for LOOP with range()
# range(start, stop, step)
# -------------------------------------------------
for i in range(5):          # 0 to 4
    print(i)

for i in range(1, 6):       # 1 to 5
    print(i)

for i in range(0, 10, 2):   # even numbers
    print(i)


# -------------------------------------------------
# 3. while LOOP
# -------------------------------------------------
count = 1

while count <= 5:
    print(count)
    count += 1


# -------------------------------------------------
# 4. break STATEMENT
# Stops the loop immediately
# -------------------------------------------------
for i in range(10):
    if i == 5:
        break
    print(i)


# -------------------------------------------------
# 5. continue STATEMENT
# Skips current iteration
# -------------------------------------------------
for i in range(5):
    if i == 2:
        continue
    print(i)


# -------------------------------------------------
# 6. pass STATEMENT
# Placeholder (does nothing)
# -------------------------------------------------
for i in range(3):
    if i == 1:
        pass
    else:
        print(i)


# -------------------------------------------------
# 7. for-else LOOP
# else runs ONLY if loop completes normally
# -------------------------------------------------
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")


# -------------------------------------------------
# 8. while-else LOOP
# -------------------------------------------------
x = 0

while x < 3:
    print(x)
    x += 1
else:
    print("While loop finished")


# -------------------------------------------------
# 9. NESTED LOOPS
# -------------------------------------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")


# -------------------------------------------------
# 10. LOOPING THROUGH STRING
# -------------------------------------------------
name = "Python"

for ch in name:
    print(ch)


# -------------------------------------------------
# 11. LOOPING THROUGH TUPLE
# -------------------------------------------------
nums = (1, 2, 3)

for n in nums:
    print(n)


# -------------------------------------------------
# 12. LOOPING THROUGH SET
# Order is NOT guaranteed
# -------------------------------------------------
unique_nums = {10, 20, 30}

for n in unique_nums:
    print(n)


# -------------------------------------------------
# 13. LOOPING THROUGH DICTIONARY
# -------------------------------------------------
student = {
    "name": "Shreyash",
    "age": 20,
    "course": "CSE"
}

# Keys only
for key in student:
    print(key)

# Values only
for value in student.values():
    print(value)

# Key + Value (BEST PRACTICE)
for key, value in student.items():
    print(key, value)


# -------------------------------------------------
# 14. enumerate()
# Gives index + value
# -------------------------------------------------
subjects = ["Math", "Physics", "DS"]

for index, subject in enumerate(subjects, start=1):
    print(index, subject)


# -------------------------------------------------
# 15. zip()
# Looping over multiple sequences
# -------------------------------------------------
names = ["A", "B", "C"]
scores = [80, 85, 90]

for name, score in zip(names, scores):
    print(name, score)


# -------------------------------------------------
# 16. INFINITE LOOP
# Use break to exit
# -------------------------------------------------
count = 0

while True:
    print("Running...")
    count += 1
    if count == 3:
        break


# -------------------------------------------------
# 17. LOOP WITH CONDITIONS (FILTERING)
# -------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    if n % 2 == 0:
        print(f"Even: {n}")


# -------------------------------------------------
# 18. COMMON MISTAKES (DOCUMENTED)
# -------------------------------------------------

# ❌ Infinite loop (forgot increment)
# while x < 5:
#     print(x)

# ✔ Correct
x = 0
while x < 5:
    print(x)
    x += 1

# ❌ Modifying list while iterating
# for n in numbers:
#     numbers.remove(n)

# ✔ Correct approach
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)
