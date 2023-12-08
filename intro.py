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

# Find - Index of where characters are found

message = 'Hello World'
print(message.find('World'))

# Replace
# Replace some characters in our string with other characters
    # Returns a new string with those values replaced, not making changes to original string

message = 'Hello World'
new_message = message.replace('World', 'Universe')
print(new_message)

# Add multiple strings and concatenate them together
    # Getting a little complicated with this syntax

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
print(message)

# Formatted Strings
# Write the sentence as it'll appear
# Put placeholders in place of variables
    # Everywhere we want to replace with a variable, we use a placeholder {}

greeting = 'Hello'
name = 'Michael'

message = '{}, {}. Welcome!'.format(greeting, name)

print(message)

# F-Strings
# Make string formatting as simple as possible
# Write the variables directly in the placeholders
# Can write directly in the placeholder (ex. {name.upper()})

greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {name}. Welcome!'

print(message)

# dir()
# Pass in a variable to get all the methods available

greeting = 'Hello'

print(dir(name))

# help()
# See what the methods do
# Type a method into the help() parameter ex. -> help(str)

greeting = 'Hello'
name = 'Michael'

print(help(str))