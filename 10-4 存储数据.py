# import json

# numbers = [2, 3, 5, 7, 11, 13]

# filename = "number.json"

# with open(filename, 'w') as f:
#     json.dump(numbers, f)

# import json

# filename = "number.json"
# with open(filename, 'r') as f:
#     numbers = json.load(f)
# print(numbers)

# username = input("What's your name?")
# filename = "username.txt"
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}!")
    
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back, {username}!")

import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What's you name?")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}")

