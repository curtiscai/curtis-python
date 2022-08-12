# 类
# 创建和使用类
# 创建类
class Dog:
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

# 根据类创建实例
my_dog = Dog("wangcai", 10)
print(f"the name of the dog is {my_dog.name}, the age of the dog is {my_dog.age}")

my_dog = Dog("wangcai", 10)
my_dog.sit()
my_dog.roll_over()

# 使用类和实例

