class Dog:
    """一次模拟小狗简单的尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name.title()
        self.age = age
    
    def sit(self):
        """模拟小狗收到命令是蹲下"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
