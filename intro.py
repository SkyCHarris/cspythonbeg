# Print Welcome Message
print('Hello World')

# Multi-line String

message = """Bobby's World
was a good
cartoon in the 1990s"""

# Can think of a string as a string of individual characters

message = 'Hello World'
print(len(message))

# Access characters

message = 'Hello World'

print(message[0])

# Slice

message = 'Hello World'
print(message[0:5])

# Slice condensed

message = 'Hello World'
print(message[:5])

# Access 'World'

message = 'Hello World'
print(message[6:])

# Data types we'll use have access to a lot of functionality via methods
# Functions and methods are basically same thing 
    # but method is a function that belongs to an object

message = 'Hello World'
print(message.lower())

# Count (characters in string)

message = 'Hello World'
print(message.count('l'))