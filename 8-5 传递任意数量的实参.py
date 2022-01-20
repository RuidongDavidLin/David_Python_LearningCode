# def make_pizza(*topppings):
#     """打印顾客点的所有配料。"""
#     print(topppings)
    
# make_pizza('pepperoni')
# make_pizza('mushroom','green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     """概述要制作的pizza"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"{topping}")
# make_pizza('pepperoni')
# make_pizza('mushroom', 'green peppers', 'extra cheese')

# def make_pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print(f"\nMakeing a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping.title()}")
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mashroom', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstain', location= 'princeton', field = 'physics')
print(user_profile)

