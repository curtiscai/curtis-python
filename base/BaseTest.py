
# 第2章　变量和简单数据类型
# 2.1 变量
print("hello world")

message = "Hello World"
print(message)

message = "Hello My World"
print(message)

# 2.2 字符串
# 字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号
message = "A B C"
print(message)
message = 'A B C'
print(message)
message = "A B 'C'"
print(message)
message = 'A B "C"'
print(message)
message = "A 'B' \"C\" D"
print(message)

## 2.2.1 使用方法修改字符串的大小写
# 方法title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
# 要将字符串改为全部大写或全部小写
name = "curtis cai"
print(name.title())
print(name.upper())
print(name.lower())
print("CURTISCai".lower())

# 2.2.2 在字符串中使用变量
first_name = "curtis"
last_name = "cai"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

# 2.2.3 Python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法rstrip()
language = " python     "
print(language.rstrip())
print(language.lstrip())
print(language.strip())

# 2.3 数
int_val = 1 + 2 * 3
print(int_val)

int_val_2 = 2 ** 3
print(int_val_2)

int_val_3 = 3 / 2
print(int_val_3)

# 3.3333333333333335
int_val_4 = 10 / 3
print(int_val_4)

# 2.4 浮点数
decimal_val_1 = 0.1 + 0.1
print(decimal_val_1)

# 0.30000000000000004
decimal_val_2 = 0.1 + 0.2
print(decimal_val_2)
# 0.30000000000000004
decimal_val_3 = 0.1 * 3
print(decimal_val_3)

# 将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除
# 2.0
val_1 = 4 / 2
print(val_1)

# 无论是哪种运算，只要有操作数是浮点数，Python默认得到的总是浮点数，即便结果原本为整数也是如此。
# 3.0
val_2 = 1 + 2.0
print(val_2)
# 6.0
val_3 = 2 * 3.0
print(val_3)

# 2.5 同时给多个变量赋值
# 可在一行代码中给多个变量赋值，这有助于缩短程序并提高其可读性。需要用逗号将变量名分开；对于要赋给变量的值，也需同样处理
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# 2.6 常量
# 常量类似于变量，但其值在程序的整个生命周期内保持不变。Python没有内置的常量类型，但Python程序员会使用全大写来指出应将某个变量视为常量，其值应始终不变
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
# 这样做语法不会有错，但是不建议。如果认定是常量则除了使用大写字母外，不应该再修改它的值
MAX_CONNECTIONS = 6000
print(MAX_CONNECTIONS)

# 2.7 注释
# 在Python中，注释用井号（#）标识。井号后面的内容都会被Python解释器忽略

import this










