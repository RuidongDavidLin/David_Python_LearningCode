import math

# for value in range(1, 5):
#     print(value)

# for value in range(1, 6):
#     print(value)

# numbers = list(range(1, 5))
# print(numbers)

# even_numbers = list(range(2, 20, 3))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
#     print(squares[value - 1]) # 思考下为什么这里要减一

# digits = list(range(1, 100, 3))
# min = min(digits)
# max = max(digits)
# sum = sum(digits)
# print(f'max = {max}, min = {min}, sum = {sum}')

# squares = [value ** 2 for value in range(1, 100, 3)]
# print(squares)

# for value in range(1, 21):
#     print(value)

# list = list(range(1,1001))
# for value in range(1, 1001):
#     print(list[value - 1])

# index = list(range(1, 1001))
# print(f'min = {min(index)}, max = {max(index)}, sum = {sum(index)}')

# odd_number = list(range(1, 20, 2))
# for value in range(1, 20, 2):
#     print(odd_number[round((value - 1)/2)])

# numbers_three = list(range(3, 31, 3))
# for value in range(3, 31, 3):
#     print(numbers_three[math.trunc((value-3)/3)])

# index = []
# for value in range(1,11):
#     index.append(value ** 3)
# for value in range(1, 11):
#     print(index[value - 1])

cubic_numbers = [cubic_number ** 3 for cubic_number in range(1, 11)]
print(cubic_numbers)