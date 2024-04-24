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

print(min(squares))
print(max(squares))
print(sum(squares))

#using list comprehension
squares_comprehension = [values ** 2 for values in range(1, 11)]
print(squares_comprehension)

#slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

players_copy = players[:]
print(players_copy)

#these are deep copies, changing the original list does not affect the copied list

#Tuples
# these are lists that are immutable, but they can be redefined wholly

dimensions = (2,50)
