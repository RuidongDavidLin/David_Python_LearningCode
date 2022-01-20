import os
# def greet_users(names):
#     """向列表中的每位用户发出简单的问候。"""
#     for name in names:
#        msg = f"Hello, {name.title()}"
#        print(f"\n{msg}")
       
# users = ["david", "kelly", "eason"]
# greet_users(users)

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design.title()}")
        completed_models.append(current_design)
def show_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model.title())

unprinted_designs = ["dog", "cat", "robot"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_models(completed_models)