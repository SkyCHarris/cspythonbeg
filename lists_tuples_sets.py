
#! Lists, Tuples, and Sets

# Lists/Tuples allow us to work with sequential data
# Sets are unordered collections of values with no duplicates

# Lists

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)

# len of list

courses = ['History', 'Math', 'Physics', 'CompSci']

print(len(courses))

# Access values

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[3])

# Last index

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[-1])

# Index range

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[0:3]) # same as [:3]


#? Lists []


#* Add item to list

# Append
# Add item to end of list

courses = ['History', 'Math', 'Physics', 'CompSci']

courses.append('Art')

print(courses)

# Insert
# Add item to specific location
# First parameter index, 2nd parameter replacement

courses = ['History', 'Math', 'Physics', 'CompSci']

courses.insert(0, 'Art')

print(courses)

# Extend
# Used when we have mult. values we want to add to our list

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.insert(0, courses_2)

print(courses)
# This method (insert) adds a list inside of a list

# Use extend to add new list to end of previous list
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.extend(courses_2)

print(courses)

#* Remove values from list

# Remove
# Takes out specified item from list

courses = ['History', 'Math', 'Physics', 'CompSci']

courses.remove('Math')

print(courses)

# Pop
# Removes last item from list (by default)


courses = ['History', 'Math', 'Physics', 'CompSci']

courses.pop()

print(courses)

# Pop returns the value that it removed

courses = ['History', 'Math', 'Physics', 'CompSci']

popped = courses.pop()

print(courses)
print(popped)

#* Sort lists

# Reverse
# Reverse our list as it currently is

courses = ['History', 'Math', 'Physics', 'CompSci']

courses.reverse()

print(courses)

# Sort
# (Letters -> Alphabetical)
# (Num -> ascending)
# Sorts the list in place

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

courses.sort()
nums.sort()

print(courses)
print(nums)

# Descending sort

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

# Sorted
# Sorted version of our list without altering original list

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

sorted_courses = sorted(courses)
sorted_nums = sorted(nums)

print(sorted_courses)
print(sorted_nums)

# Index
# Find values in list
# Find index of a certain value

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('CompSci'))

# For loops

courses = ['History', 'Math', 'Physics', 'CompSci']

for item in courses:
    print(item)

# Enumerate
# Get value and index

courses = ['History', 'Math', 'Physics', 'CompSci']

for course in enumerate(courses):
    print(course)

# Can take start value/parameter

courses = ['History', 'Math', 'Physics', 'CompSci']

for course in enumerate(courses, start=1):
    print(course)

# join()
# Turn lists into strings, separated by a certain value
# join() is string method, list passed in as argument

courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = '-'.join(courses)

print(course_str)

# split()
# Do the reverse, turn a string back into a list

courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = '-'.join(courses)

new_list = course_str.split('-')

print(new_list)


#? Tuples ()
# Can't modify. Immutable.

# Mutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)
# Both list_1 and list_2 have the same values

# Change value in index 0 of list 1, then reprinting again

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

list_1[0] = 'Art'

print(list_1)
print(list_2)
# They're both the same mutable object

# If you want a list of values that you know aren't gonna change, use a tuple

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Since tuple is immutable, many less methods
# Can't append, remove, etc.
print(dir(tuple_1))


#? Sets {}
# Values that are unordered and have no duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)

# Sets don't really care about order

# UseCases
# 1. Test whether a value is part of a set
# 2. Remove duplicate values

#2. 
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)

#1. (membership test)
# (more efficient than lists/tuples)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print('Math' in cs_courses)

# Intersection
# Sets can quickly determine what values they share/don't share with other sets

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))

# Difference
# Which courses are in cs_courses but not art_courses

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.difference(art_courses))

# Union
# Combine both sets and print all courses offered

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} #! Not right! It's a dictionary
empty_set = set() #* Just this way to create empty set