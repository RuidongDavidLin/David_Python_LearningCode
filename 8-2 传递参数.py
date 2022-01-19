# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type} 's name is {pet_name.title()}")

# describe_pet('hamster', 'harry')
# describe_pet('acd', "as")

#这里应该会有一个代码的，但是我写完才发现它是一个错误示例，所以我把它删掉了……

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type} 's name is {pet_name.title()}")
describe_pet(animal_type= "dog", pet_name= "hamberger")

def describe_pet(animal_type, pet_name = "hamburger"):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} 's name is {pet_name.title()}")
describe_pet("pet")
describe_pet("dog", "will")