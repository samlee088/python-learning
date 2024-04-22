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

