"""
Working With Lists
"""


magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)
    print(f"{magician}, that was a great trick!")
    print(f"I can't wait for your next trick {magician}. \n")

number_list = list(range(5))
print(number_list)

number_list_even = list(range(2, 11, 2))
print(number_list_even)

squares = []
for number in range(1, 11):
    value = number ** 2
    squares.append(value)
print(squares)

squares = []
for number in range(1, 11):
    squares.append(number **2)
print(squares)