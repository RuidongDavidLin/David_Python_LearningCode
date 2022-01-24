# file_name = "programming.txt"
# with open(file_name, 'w') as file_object:
#     file_object.write("I do love programming!")

file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I do love programming.\n")
    file_object.write("I do love creating new games.\n")
with open(file_name, 'a') as file_object:
    file_object.write("hiahiahiahia!")