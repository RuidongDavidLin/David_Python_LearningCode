# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[0].title())

# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles.append('honda')
# print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles.insert(3, 'halei')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# del motorcycles[0]
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# motorcycles.pop()

# print(motorcycles)
# print(popped_motorcycle)
# last_owned = motorcycles.pop()
# message = f'The last motorcycle I owned was a {last_owned}'
# print(message)
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
message = f'\nA {too_expensive} is too expensive for me!'
print(message)
