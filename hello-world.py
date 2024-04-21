print("Hello Python World")

message = "Hello World"
print(message)
message = "Hello World Updated"
print(message)

#This is a forced message to view a error message
# error_message_view = "This is error test"
# print(eror_message_view)

"""
Strings
"""

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "Yugi"
last_name = "Moto"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

#Spaces and tab spaces
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavascript")
print("Languages:\n\tPython\n\tC\n\tJavascript")

#Stripping whitespace
favorite_language = " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#Removing Prefixes
nostarchUrl = 'https://nostarch.com'
print(nostarchUrl.removeprefix('https://'))

"""
Numbers
"""

# Python typically will default to float for number format post equation result

wealth = 14_000_000_000
print(wealth)

#Python simply will ignore the underscores for numbers, these two fill print the same number for example
thousand_1 = 1_000
thousand_2 = 10_00
print(thousand_1)
print(thousand_2)

#Multiple assignment to variables
x,y,z = 0,1,2
print(x,y,z)

#Constant is a variable that has a value that stays the same throughout the life of a program. These are typically written in all caps as syntax
MAX_CONNECTIONS = 500

taxi_cab_number = 1729
print(f"This is an example of a taxi-can number: {taxi_cab_number}")