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


