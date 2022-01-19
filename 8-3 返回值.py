# def formatted_name(first_name, second_name):
#     full_name = first_name.title() + " " + second_name.title()
#     return full_name
# name = formatted_name("David", "Lin")
# print(name)

# def formatted_name(first_name, last_name, middle_name=""):
#     full_name = first_name + middle_name + last_name
#     return full_name.title()

# full_name = formatted_name("David", " Lin", " ruidong")
# print(full_name)
# full_name = formatted_name("david", " lin")
# print(full_name)

# def build_person(first_name, last_name):
#     person = {'first':first_name, 'last':last_name}
#     return person
# person = build_person("David", " Lin")
# print(person)

# def build_person(first_name, last_name, age = None):
#     person = {"first":first_name, "last":last_name}
#     if age:
#         person["age"] = age
#     return person
# person = build_person("David", "Lin", age = 20)
# print(person)
# person = build_person("David", "Lin")
# print(person)

def formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    first_name = input("First name:")
    if first_name == "quit":
        print("That's all, thank you!")
        break
    last_name = input("last name:")
    full_name = formatted_name(first_name, last_name)
    print(f"\nHello, {full_name}")
