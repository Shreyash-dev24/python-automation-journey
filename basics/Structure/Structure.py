"""
Python List Operations
----------------------
This file demonstrates common operations performed on Python lists:
- Creation
- Accessing elements
- Insertion
- Removal
- Looping
- Joining and splitting
"""

# -------------------------------
# 1. Creating a List
# -------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']


# -------------------------------
# 2. Accessing Elements (Slicing)
# -------------------------------
# print(courses)          # Prints full list
# print(courses[:2])      # Prints first two elements


# -------------------------------
# 3. Exploring List Methods
# -------------------------------
# print(dir(list))            # Shows all list methods
# print(help(list.append))   # Explains append() method


# -------------------------------
# 4. Inserting Elements
# -------------------------------
courses_2 = ['dbms', 'NIS']

# courses.append('Art')            # Adds element at the end
# courses.insert(0, 'Geography')   # Inserts before index 0
# courses.extend(courses_2)        # Adds another list

# print(courses)


# -------------------------------
# 5. Removing Elements
# -------------------------------
courses2 = ['History', 'Math', 'Physics', 'CompSci']

# courses2.remove('Math')   # Removes specific element
# courses2.pop()            # Removes last element

# print(courses2)


# -------------------------------
# 6. Looping Through List
# -------------------------------
# enumerate() gives index + value
# for index, course in enumerate(courses, start=1):
#     print(index, course)


# -------------------------------
# 7. Joining and Splitting List
# -------------------------------
# courses_str = ' - '.join(courses)    # List → String
# new_list = courses_str.split(' - ')  # String → List

# print(courses_str)
# print(new_list)
 

"""
Tuple Operations
----------------
Tuples are ordered and immutable collections.
Once created, elements cannot be modified.
"""

# -------------------------------
# 1. Creating a Tuple
# -------------------------------
courses = ('History', 'Math', 'Physics', 'CompSci')


# -------------------------------
# 2. Accessing Elements
# -------------------------------
# print(courses)        # Full tuple
# print(courses[0])     # First element
# print(courses[:2])    # Slicing works like lists


# -------------------------------
# 3. Tuple Immutability
# -------------------------------
# courses[0] = 'Art'    # ❌ Error: Tuples cannot be modified


# -------------------------------
# 4. Looping Through Tuple
# -------------------------------
# for course in courses:
#     print(course)


# -------------------------------
# 5. Tuple with One Element
# -------------------------------
single = ('Math',)      # Comma is mandatory
# print(type(single))



"""
Set Operations
--------------
Sets store unique elements.
They are unordered and do not support indexing.
"""

# -------------------------------
# 1. Creating a Set
# -------------------------------
courses = {'History', 'Math', 'Physics', 'CompSci'}


# -------------------------------
# 2. Properties of Set
# -------------------------------
# print(courses)        # Order is not guaranteed
# print('Math' in courses)   # Fast membership test


# -------------------------------
# 3. Adding Elements
# -------------------------------
# courses.add('Art')
# courses.update(['DBMS', 'NIS'])

# print(courses)


# -------------------------------
# 4. Removing Elements
# -------------------------------
# courses.remove('Math')     # Error if element not found
# courses.discard('Math')    # Safe removal
# courses.pop()              # Removes random element

# print(courses)


# -------------------------------
# 5. Set Operations
# -------------------------------
set1 = {'Math', 'Physics', 'CompSci'}
set2 = {'Physics', 'Biology', 'Chemistry'}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))


"""
Dictionary Operations
---------------------
Dictionaries store data as key-value pairs.
Keys must be unique.
"""

# -------------------------------
# 1. Creating a Dictionary
# -------------------------------
student = {
    'name': 'Shreyash',
    'age': 20,
    'course': 'CSE'
}


# -------------------------------
# 2. Accessing Values
# -------------------------------
# print(student['name'])          # Direct access
# print(student.get('age'))       # Safe access
# print(student.get('phone'))     # Returns None


# -------------------------------
# 3. Adding / Updating Values
# -------------------------------
# student['phone'] = '9999999999'
# student['age'] = 21

# print(student)


# -------------------------------
# 4. Removing Elements
# -------------------------------
# student.pop('age')
# del student['course']

# print(student)


# -------------------------------
# 5. Looping Through Dictionary
# -------------------------------
# for key in student:
#     print(key, student[key])

# for key, value in student.items():
#     print(key, value)


# -------------------------------
# 6. Dictionary Keys, Values, Items
# -------------------------------
# print(student.keys())f
# print(student.values())
# print(student.items())

