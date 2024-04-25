from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)

path = Path('pi_million_digits.txt')

line_contents = path.read_text().splitlines()

pi_content = ""

for line in line_contents:
    pi_content += line.lstrip()

print(pi_content[:50])
print(len(pi_content))

birthday = input("Please enter your birthday mmddyy: ")

if birthday in pi_content:
    print("Your birthday is in the first million digits of pi")
else:
    print("Your birthday is not in the first million digits of pi")