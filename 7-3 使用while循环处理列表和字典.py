# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []
# current_number = 0

# for user in unconfirmed_users:
#     unconfirmed_users[current_number] = user.title()
#     current_number += 1

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user:{current_user.title()}")
#     print(f"Unverifying user:{unconfirmed_users}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for user in confirmed_users:
#     print(user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name?")
    reponse = input("\nWhich mountain would you like to climb someday?")
    responses[name] = reponse
    repeat = input("\nWould you like to let another person respond? (Yes/No)")
    if repeat.title() == 'No':
        polling_active = False
print("\n---Poll Results ---")
for name,response in responses.items():
    print(f"{name.title()} would like to climb {response}")