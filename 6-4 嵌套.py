# alien_0 = {'color': 'green', 'point': 5}
# alien_1 = {'color': 'yellow', 'point': 10}
# alien_2 = {'color': 'red', 'point': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_number in range(0,30):
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[0:5]:
#     print(alien)
# print("...")

# print(f"Total number of aliens: {len(aliens)}")

# aliens = []

# for alien_number in range(0,30):
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['point'] = 10
#         alien['speed'] = 'slow'

# for alien in aliens[0:5]:
#     print(alien)

# pizza = {
#     'curst': 'thick',
#     'topping': ['mushroom', 'extra cheese'],
# }

# print(f"You ordered a {pizza['curst']}-curst pizza "
#     "with the following toppings:")

# for topping in pizza['topping']:
#     print("\t" + topping)

# favorite_language = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for name,languages in favorite_language.items():
#     print(f"\n{name.title()} 's favorite language are:")
#     for language in languages:
#         print(f"\t{language.title()}")

from distutils.command.build_scripts import first_line_re


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'aeinstain',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"Username:{username}")
    fullname = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {fullname.title()}")
    print(f"\tLocation: {location.title()}")