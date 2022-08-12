# 函数
# 函数定义
# 文档字符串（docstring）的注释，描述了函数是做什么的。文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。
def func_test():
    """this is a note of function"""
    print("this is a function")


func_test()


def func_test(name):
    """this is a note of funtion"""
    print(f"Hello, {name.title()}")


func_test("curtis")


# 传递实参
# 函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多：可使用位置实参，这要求实参的顺序与形参的顺序相同；
# 也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。

# 位置实参
# Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式称为位置实参。
def province_city(province, city):
    print(f"the city {city} is in the province of {province}")


province_city("河北", "石家庄")

# 关键字实参
# 关键字实参是传递给函数的名称值对。因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。
# 关键字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。

province_city(province="河北", city="石家庄")


# 默认值
def province_city(province="北京", city="北京"):
    print(f"the city {city} is in the province of {province}")


province_city()
province_city(province="首都")
province_city(city="首都")
province_city("河北", "石家庄")


# 返回值
def get_full_name(first_name, last_name=""):
    full_name = f"full_name = {first_name} {last_name}"
    return full_name.title()


full_name = get_full_name("cai", "curtis")
print(full_name)
full_name = get_full_name("cai")
print(full_name)
full_name = get_full_name(first_name="cai", last_name="curtis")
print(full_name)


def build_full_name(first_name, last_name, age=None):
    full_name = {"first_name": first_name, "last_name": last_name}
    if age:
        full_name["age"] = age
    return full_name


full_name = build_full_name(first_name="cai", last_name="curtis")
print(full_name)
full_name = build_full_name(first_name="cai", last_name="curtis", age=21)
print(full_name)


# 向函数传递列表
def print_user(names):
    for name in names:
        print(name)


names = ["curtis1", "curtis2", "curtis3"]
print_user(names)


