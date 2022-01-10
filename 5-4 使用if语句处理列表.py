# requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'mushroom':
#         print("Sry, we are out of mushroom right now.")
#     else:
#         print(f"Adding {requested_topping}")

# print("\nFinish making your pizza")

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ['mushroom', 'olives', 'green peppers', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Add {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")
