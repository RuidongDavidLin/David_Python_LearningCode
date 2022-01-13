# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f'\nKey: {key.title()}')
#     print(f'Value: {value.title()}')

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# for key, value in favorite_language.items():
#     print(f"\nKey: {key.title()}")
#     print(f"Value:{value.title()}")

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_language.items():
#     print(f"\nName: {name.title()}")
#     if name == 'jen':
#         print(f"{name.title()}'s favorite language is {language.title()}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'foden': 'python',
    'kevin': 'python',
}

for value in favorite_languages.values():
    print(f"value is {value.title()}")

for value in sorted(favorite_languages.values()):
    print(f"value is {value}")

for value in set(favorite_languages.values()):
    print(value)

for value in sorted(set(favorite_languages.values())):
    print(value)

language = {'python', 'C sharp', 'Cpp'}
print(language)

print(favorite_languages)
