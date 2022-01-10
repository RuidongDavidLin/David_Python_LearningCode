# players = ['charles', 'martina', 'michael', 'florance', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])
# print(players[0::2])

# print("Here are the first three players on my team:")
# for player in players[0:3]:
#     print(player.title())

# 复制列表
# my_foods = ['pizza', 'falafel', 'carrot cake'] #falafel 炸豆丸子 n.
# friends_food = []
# for food in my_foods:
#     friends_food.append(food)
# print(friends_food)
# 上面是我自己写的，不是书本上的方法

# friends_food = my_foods[:]
# print("My favorites food are :")
# print(my_foods)

# print("\nMy friends' favorite food are :")
# print(friends_food)

# my_foods.append('cannoli')
# friends_food.append('ice cream')
# print(my_foods)
# print(friends_food)

# Practice
my_girlfriends = ['liu yifei', 'dilireba', 'tong liya', 'wang bingbing', 'zhang yang']
print("The first three girlfriends of mine are:")
my_first_three_girls = my_girlfriends[0:3]
for girl in my_first_three_girls:
    print(girl.title())

my_medium_three_girls = my_girlfriends[1:4]
for girl in my_medium_three_girls:
    print(girl.title())

my_last_three_girls = my_girlfriends[-3:]
for girl in my_last_three_girls:
    print(girl.title())

