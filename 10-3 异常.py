# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero.")


# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# try:
#     while True:
#         first_num = input("\nFirst number:")
#         if first_num == 'q':
#             break
#         second_num = input("\nSecond number:")
#         if second_num == 'q':
#             break
#         answer = int(first_num)/int(second_num)
#         print(answer)
# except ZeroDivisionError:
#     print("You can't divide by zero.")

from encodings import utf_8


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, encoding = 'utf_8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        with open("miss_words.txt", 'a') as f:
            f.write(f"\n{filename} is not found!")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'lice.txt'
count_words(filename)