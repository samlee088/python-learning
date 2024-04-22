"""
Learning about lists
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('harley')
print(motorcycles)
motorcycles.insert(2, 'kawasaki')
print(motorcycles)

#Deleting items from a list
#position based method del, delete if position is known
del motorcycles[2]
print(motorcycles)

removed = motorcycles.pop()
removed_with_position = motorcycles.pop(1)

#del should be used when deleting an item from a list and not use that item. pop should be used when I want to remove an item from a list and use it

print(motorcycles)
motorcycles.remove('suzuki')
#remove can be stored for later use in a variable. it also will only remove the first instance of a match

#Organizing a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)

cars.reverse()
print(cars)
cars.reverse()
print(cars)

print(len(cars))

"""
Working With Lists
"""



